# AudioVision
*A navigation tool for the visually impaired.*
***
## Overview
The main script that operates the breadbox is written in Python.
The install script and the initialization script are shell scripts.

AudioVision is a tool for the visually impaired, specifically designed to help blind people move around.
The device uses an Ultrasonic Ranging Module to measure distance and a buzzer to produce beeps.
The closer you are to an object, the more frequent the buzzer beeps.

By gauging the speed of the beeps, visually impaired individuals are able to get a sense of the distance between them and objects they point the sensor toward.
While canes can tell them what is directly in front of you, they cannot tell you how far you are from an object until you are right against it.

## Installation
In order to use this program, simply download the INSTALL folder, give the three files within executable permissions, and run the setup.sh file. This can all be done using SSH or VNS, so there is no need to connect your RaspberryPi to a monitor. Once you run the setup.sh script, the startup.sh script will be added to crontab to run on reboot, and then the setup script will be deleted. The python script will also start at this time.

## Usage
Once the setup script has been run, the RaspberryPi will begin interacting with the breadboard. At this point, you can disconnect from SSH and/or VNS and the RaspberryPi no longer needs to be configured. There is a red button on the breadboard; This button shuts down the RaspberryPi and hence the program. This mixed with the crontab startup script function as the on/off for the project. After pressing the red button, wait a few seconds for the RaspberryPi to properly shut down and then unplug the power source. When you wish to enable the machine once again, plug back in the power source and wait ~15 seconds to give it time to boot. The script will then start automatically and the beeping will begin. 
