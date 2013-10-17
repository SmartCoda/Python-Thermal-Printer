from __future__ import print_function
import RPi.GPIO as GPIO
import subprocess, time, Image, socket
from Adafruit_Thermal import *

printer = Adafruit_Thermal("/dev/ttyAMA0", 19200, timeout=5)

# Print greeting image
# Because the hello/goodbye images are overall fairly light, we can
# get away with using a darker heat time for these, then reset to the
# default afterward.
ht = printer.defaultHeatTime * 2
if(ht > 255): ht = 255

printer.begin(ht) # Set temporary dark heat time
printer.println("Colour")
printer.printImage(Image.open('gfx/partlycloudy.gif'), True)
printer.feed(3)
printer.println("Greyscale")
printer.printImage(Image.open('gfx/result.png'), True)
printer.feed(3)
printer.println("B&W")
printer.printImage(Image.open('gfx/result.gif'), True)
printer.feed(3)
printer.begin() # Reset default heat time

