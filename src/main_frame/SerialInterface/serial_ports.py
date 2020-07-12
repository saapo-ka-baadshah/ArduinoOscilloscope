"""
Created by Amey on 11/07/2020
"""

import serial.tools.list_ports as lp

def getArduinoDevice():
    """
    Returns the Arduino Manufactured Device
    >>> getArduinoDevice()

    :return: Serial InterFace
    """

    for i in list(lp.comports()):
        if("Arduino" in str(i.manufacturer)):
            return(i)

    return(None)
