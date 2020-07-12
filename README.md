# Arduino Oscilloscope
For many developments an Oscilloscope is much needed. And when it comes to pricing it is not a really friendly choice to buy one. 

We have a lot of options with **the Microsoft Windows** which can make the Arduino solve the purpose by displaying input signals on your computer. 

But when it comes to **Linux**, one with immense efforts can find only a few options which may or may not work on every machine. 

**So here's a solution for this. Arduino Oscilloscope.**


---
## Prerequisite
- **An Arduino Clone** (Currently only arduinos with Specific Serial Descriptions are suppored)
- **Python 3.x.x**
- **Creativity to help this project grow**

---

## Installation

- Download this Repo and Extract it to a location of your choice
- Open a terminal in the same location
- Enter Following commands: 
```bash
sudo chmod +x oscilloscope.sh setup.sh
sh setup.sh
```
- This will create a Desktop Shortcut for your application
- Double click on it and 'Trust and Launch' the application

<!-- ![Trust and Launch](https://jmp.sh/RLSjNyD) -->

---
## Hardware Restrictions
- **Minimum Input Voltage: 0V**
- **Maximum Input Voltage: 5V**
- **Sampling rate: O(16 MHz)** 

---
## Changelogs
- Memory Management Thread added
- Support for Arduinos with the Serial Manufacturer description containing the string "Arduino"

---
## For Additional Support

If you find the Manufaturer Description for your device's Serial interface, Add the Manufacturer Detail to the SUPPORTED_DEVICES list from following file location: 

> src/main_frame/SerialInterface/serial_ports.py

Don't forget to add a fork to improve the support for devices.
