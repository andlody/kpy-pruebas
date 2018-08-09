from _libs.kurmix.Controller import *

class calculadora_controller(Controller):
	def index(this):
		this.write('<br>Hola desde calculadora')

	def before(this):
		this.write('<br>before calcula')



	def after(this):
		this.write('<br>aftere calcula')

	