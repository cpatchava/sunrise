import requests

class Particle:
	
	def __init__(self, device_id, access_token):
		self.device_id = device_id
		self.access_token = access_token
	
	def post(self, function, key, value):
		post_url="https://api.particle.io/v1/devices/%(id)s/%(function)s?access_token=%(access_token)s" % {'id': self.device_id, 'function': function, 'access_token': self.access_token}
		r = requests.post(post_url, data = {key : value})

	def turn_on(self):
		self.post("led", "arg", "on")

	def increase_light(self):
		self.post("led", "arg", "up")
	
	def decrease_light(self):
		self.post("led", "arg", "down")

	def turn_yellow(self):
		self.post("led", "arg", "yellow")
	
	def turn_orange(self):
		self.post("led", "arg", "orange")
	
	def turn_light_orange(self):
		self.post("led", "arg", "light_orange")
	
	def turn_sky_blue(self):
		self.post("led", "arg", "sky_blue")

	def turn_white(self):
		self.post("led", "arg", "white")
	
	def turn_green(self):
		self.post("led", "arg", "green")

	def turn_blue(self):
		self.post("led", "arg", "blue")
	




