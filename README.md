# Arduino Oscilloscope
For many developments an Oscilloscope is much needed. And when it comes to pricing it is not a really friendly choice to buy one. 

We have a lot of options with **the Microsoft Windows** which can make the Arduino solve the purpose by displaying input signals on your computer. 

But when it comes to **Linux**, with immense efforts one can find only a few options which may or may not work on every machine. 

**So here's a solution for this. Arduino Oscilloscope.**


---
## Prerequisite
- **An Arduino Clone** (Currently only arduinos with Specific Serial Descriptions are suppored)
- **Python 3.x.x**
- **Creativity to help this project grow**

---

## Flash following Firmware on your device: 
Framework Used: Arduino (For the sake of simplicity)

Flash following code on your MCU:
``` c++

void setup(){
    Serial.begin(115200);           // Use any Baud Rate you want.
                                    // Make sure you change the
                                    // baud_rate in line 94 in:
                                    // src/main_frame/frame.py
}

void loop(){
  double probe_val = (double) analogRead(A0) ;
  double val = probe_val / ((double)1023) ;     // Step1: Step Normalization
  val = val * 5;            // Step2: Value Normalization
  Serial.print(((String)val) + " " + (String) (micros() - start_time));
  Serial.println();

}

```

Feel free to use any other framework of your choice. Make sure you normalize the input ADC data as mentioned above in the code.

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
