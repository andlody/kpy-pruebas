from _libs.kurmix.Controller import *

class index_controller(Controller):
	def index(this):
		#this.write('Holis')
		pass

	def hola(this):
		this.set("Hola mundo..!")

	def enviar_datos_vista(this):
		this.set("num",123456)
		this.set("name","Andree Ochoa")
		this.set("mail","aochoa@kurmix.org")
		this.set("json", this.json())

	def otra_plantilla(this):
		this.view("index/index")
		this.template("esmeralda")
