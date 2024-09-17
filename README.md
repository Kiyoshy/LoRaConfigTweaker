# LoRa Config Tweaker


The code contained within this repository provides the capability to adjust various parameters of your LoPy4 device: message transmission time, bandwidth allocation, setting the transmission power (tx_power), and selecting the transmission channel, all prior to initiating the transmission process. It should be noted that the code has been tested using a predefined message.

## Technical details

* [LoPy4](https://pycom.io/product/lopy4/) quadruple bearer MicroPython enabled development board. 

* [Pysense board](https://pycom.io/product/pysense-2-0-x/)

* [Expansion board](https://docs.pycom.io/datasheets/expansionboards/expansion3/)

* Firmware version: Pycom MicroPython 1.20.0.rc13 [v1.9.4-94bb382] on 2019-08-22.


## Getting started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes in your lopy.


### Prerequisites

This is the basic information required to set up a suitable development environment for a Pycom device, in this case the LoPy's.

You first need to have Python 3 and Pip 3 installed in your computer. Check here for the proper instructions and code:
```
https://www.python.org/download/releases/3.0/

$ sudo apt install python3
$ sudo apt install python3-pip
```

Install the software required to connect to the LoPy device
```
$ sudo python3 -m pip install mpy-repl-tool
```

For more information you can check the full [documentation](https://docs.pycom.io/)


### Installing

Now you can download and install the project in your devices.

First download the .ZIP, extract it in your machine.

To install the repository in the LoPy device, open a terminal on the project's location.

Verify if the device has been recognized:
```
$ sudo python3 -m there detect
```

Confirm that the device only contains the main.py and boot.py files:
```
$ sudo python3 -m there ls -l /flash/ *
```

Upload the files of the repository to the device:
```
$ sudo python3 -m there push *.py /flash
```

### Files

The code in this folder is written in MicroPython and tested on:

Files contained:

* File `boot.py` simply disables the WiFi to limit interferences.

* The `lora_sender.py` file is responsible for configuring the parameters of the device and initiating the transmission of messages. 

* The `lora_receiver.py` file handles the configuration parameters for the device and initiates the message reception procedure.


Example of a send/receive interaction (ping/pong).

![](Img/ping-pong.png)


## Experimental

Crucial: Consistent configuration on both devices is imperative for ensuring reliable communication.

The sending device should have the boot + sender files (LoPy A), whereas the receiving device should have the boot + receiver files (LoPy B).

Initially, the code should be executed on the receiver device, followed by the transmitter.

The message can be customized to accommodate specific requirements.



## Authors

* **Kiyoshy Nakamura**

## License

This project is licensed under the GNU GPLv3 - see the [LICENSE](LICENSE) file for details.