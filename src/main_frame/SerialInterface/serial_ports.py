"""
Created by Amey on 11/07/2020
"""

import serial.tools.list_ports as lp

SUPPORT_DEVICES = [
    "Arduino",
]

def getArduinoDevice():
    """
    Returns the Arduino Manufactured Device
    >>> getArduinoDevice()

    :return: Serial InterFace
    """
    global SUPPORT_DEVICES

    for i in list(lp.comports()):
        for device in SUPPORT_DEVICES:
            if("Arduino" in str(i.manufacturer)):
                return(i)

    return(None)
