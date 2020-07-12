#!/bin/bash

main_user=$(whoami)
sudo echo "Hello $main_user! This will create a shortcut to your Desktop!"

MY_PATH="`dirname \"$0\"`"
MY_PATH="`(cd \"$MY_PATH\" && pwd )`"


if [ -e ~/Desktop/Arduino\ Oscillator.desktop ]; then
  echo "Shortcut Already Exists. Please Delete the existing Shortcut from Desktop"
else
  sudo touch ~/Desktop/Arduino\ Oscilloscope.txt
  sudo chown "$main_user" ~/Desktop/Arduino\ Oscilloscope.txt
  echo "[Desktop Entry]" > ~/Desktop/Arduino\ Oscilloscope.txt
  echo "Version=1.0" >> ~/Desktop/Arduino\ Oscilloscope.txt
  echo "Type=Application" >> ~/Desktop/Arduino\ Oscilloscope.txt
  echo "Terminal=false" >> ~/Desktop/Arduino\ Oscilloscope.txt
  echo "Icon=$MY_PATH/oscilloscope.png" >> ~/Desktop/Arduino\ Oscilloscope.txt
  echo "Exec=sh $MY_PATH/oscilloscope.sh" >> ~/Desktop/Arduino\ Oscilloscope.txt
  echo "Name=Arduino Oscilloscope" >> ~/Desktop/Arduino\ Oscilloscope.txt
fi

sudo mv ~/Desktop/Arduino\ Oscilloscope.txt ~/Desktop/Arduino\ Oscilloscope.desktop
sudo chmod a+x ~/Desktop/Arduino\ Oscilloscope.desktop
sudo chown $main_user ~/Desktop/Arduino\ Oscilloscope.desktop
