#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import tornado.ioloop
import tornado.web
import tornado.websocket
import led


from tornado.options import define, options, parse_command_line

define("port", default=8888, help="run on the given port")

root = os.path.dirname(__file__)

gpioHandler = led.Handler()

class WebSocketHandler(tornado.websocket.WebSocketHandler):
	
	
	def check_origin(self, origin):
		return True

	def open(self):
		print("WebSocket opened")

	def on_message(self, message):

		if(message == "red"):
			gpioHandler.toggleRedLed()

		if(message == "green"):
			gpioHandler.toggleGreenLed()


		if(message == "yellow"):
			gpioHandler.toggleYellowLed()


		if(message == "blue"):
			gpioHandler.toggleBlueLed()


	def on_close(self):
		print("WebSocket closed")

app = tornado.web.Application([
	#~ (r'/', HtmlHandler),
	(r'/websocket', WebSocketHandler),
	(r"/(.*)", tornado.web.StaticFileHandler, {"path": root, "default_filename": "index.html"})
])

if __name__ == '__main__':
	parse_command_line()
	app.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()
