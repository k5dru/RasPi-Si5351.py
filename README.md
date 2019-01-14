RasPi-Si5351.py
================

Python library for setting the frequency of a Si5351 off the Raspberry Pi's I2C bus.

Library derived from code at https://github.com/adafruit/Adafruit_Si5351_Library


on 2019-01-12, k5dru successfully did this using a Raspberry Pi Zero W with Raspbian GNU/Linux 9 (stretch)
* git clone https://github.com/roseengineering/RasPi-Si5351.py
* pip3 install smbus2
* changed all instances of "smbus" to "smbus2" in both python files
* changed all print operators to functions
* changed the except: lines b/c python3 doesn't like that syntax
* uncommeted this line /boot/config.txt
dtparam=i2c_arm=on
* rebooted 
* ran sudo raspi-config; chose Interface Options/I2C/Enabled
* ran  python3 Si5351.py, which worked after a bit of soldering. 
on 2019-01-13: 
* added in the set frequency function 
* modified the set frequency function to work below 600khz (for low amateur radio band operation)
* ported an old Arduino project to generate morse code to a Python class
* created a simple 10 meter beacon (using an external low pass filter on the Si5351a)
