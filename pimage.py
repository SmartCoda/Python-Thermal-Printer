
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
image_file = Image.open('gfx/partlycloudy.gif')
image_100 = image_file.resize((100,100),Image.ANTIALIAS)
image_200 = image_file.resize((200,200),Image.ANTIALIAS)
image_file = image_file.convert('L')
image_100 = image_100.convert('L')
image_200 = image_200.convert('L')
printer.println("Image 50x50")
printer.printImage(image_file, True)
printer.feed(3)
printer.println("Image 100x100")
printer.printImage(image_100, True)
printer.feed(3)
printer.println("Image 200x200")
printer.printImage(image_200, True)
printer.feed(3)
printer.begin() # Reset default heat time

