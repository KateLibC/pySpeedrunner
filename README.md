# pySpeedrunner

pySpeedrunner is a WIP. It intends to provide a cross-platform speedrunning 
timer using Python 3, Socket.IO and JQuery. 

As it stands right now, it's a glorified timer that uses a static split 
display and has no inputs at the moment. Literally it is being put on GitHub 
so I have motivation to keep working on it.

## Plans

* Incorporate splits.io into it for new split data sources
* Timer with checks against NTP or using local system time against process time
* Use LibUSB/HIDAPI to interact with HID-based foot pedals
* Create a control panel for use via mobile phones
* Allow for custom CSS based for individual splits files
* Export options to other speedrunner timer formats
* Support for control over serial ports for Arduino and likewise devices

## Current status

It's literally a glorified timer right now.

## Use

You will require the following:

* Python 3
* Flask
* Flask-socketio

Using any operating system, you can execute it as follows:

`python3 main.py`

A service will listen on port 5000 at which point you can connect to the 
following URL:

> http://localhost:5000

This service runs in debug-mode by default as it is not in production, so 
do not expose this to your network as it is a security risk.