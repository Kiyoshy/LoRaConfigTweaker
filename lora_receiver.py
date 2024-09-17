# PyCom LoPy4 documentation: 
# https://docs.pycom.io/firmwareapi/pycom/network/lora/
# https://alepycom.gitbooks.io/pycom-documentation/content/chapter/firmwareapi/pycom/network/lora.html


from network import LoRa
import socket
import time

# User requirements
# Data transmission time
inter = int(input("Interval time (ms): "))
interval = (inter/1000)

# Bandwidth choice
bw_valid = False
while not bw_valid:
    bandw = int(input("Enter bandwidth (125/250/500) KHz: "))
    if bandw == 125:
        bw = LoRa.BW_125KHZ
        bw_valid = True
    elif bandw == 250:
        bw = LoRa.BW_250KHZ
        bw_valid = True
    elif bandw == 500:
        bw = LoRa.BW_500KHZ
        bw_valid = True
    else:
        print("Invalid bandwidth, please choose an valid option")

# Tx power choice
tx_p_valid = False
while not tx_p_valid:
    tx_p = int(input("Choose tx_power (2-14): "))
    if tx_p >= 2 and tx_p <= 14:
        tx_pw = tx_p
        tx_p_valid = True
    else:
        print("Invalid tx_power, please choose a value between 2 and 14")


# LoRa Configuration
lora = LoRa(mode         = LoRa.LORA, 
            region       = LoRa.EU868,
            frequency    = 868000000,
            tx_power     = tx_pw,
            bandwidth    = bw,
            sf           = 7,
            preamble     = 8,
            coding_rate  = LoRa.CODING_4_5,
            power_mode   = LoRa.ALWAYS_ON,
            tx_iq        = False,
            rx_iq        = False,
            public       = True,
            tx_retries   = 1,
            device_class = LoRa.CLASS_A)

#Initialize LoRa
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)

# Channel selection
def set_transmit_channel(channel):
    if channel in range(0, 15):  # Accepts values between 0 and 15 for EU 
        lora.add_channel(index=channel, frequency=868000000, dr_min=0, dr_max=6)
        return True
    else:
        print("Invalid channel, please select a channel between 0 and 15")
        return False  # Indicate that the channel is invalid

channel_valid = False
while not channel_valid:
    channel_number = int(input("Select transmission channel (0-15): "))
    channel_valid = set_transmit_channel(channel_number)

# Message reception
i = 0
while True:
    if s.recv(128) == b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
        print('Ping {}'.format(i))
        i= i+1
    time.sleep(interval)