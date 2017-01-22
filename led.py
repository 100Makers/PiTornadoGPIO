#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO

class Led:
	def __init__(self,name,pin):
		self.name = name
		self.pin = pin
		self.status = False
		GPIO.setup(pin, GPIO.OUT)

	def on(self):
		print self.name + " led on"
		GPIO.output(self.pin, GPIO.HIGH)
		self.status = True

	def off(self):
		print self.name + " led off"
		GPIO.output(self.pin, GPIO.LOW)
		self.status = False
	
	def toggle(self):
		if(self.status):
			self.off()
		else:
			self.on()


class Handler:
	def __init__(self):
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
		self.red 	= Led('red',21)
		self.green 	= Led('green',20)
		self.yellow	= Led('yellow',16)
		self.blue	= Led('blue',19)

	def toggleRedLed(self):
		self.red.toggle()

	def toggleGreenLed(self):
		self.green.toggle()

	def toggleYellowLed(self):
		self.yellow.toggle()

	def toggleBlueLed(self):
		self.blue.toggle()


