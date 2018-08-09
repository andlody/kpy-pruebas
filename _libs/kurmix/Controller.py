# =======  Kurmix  =======                           _  __   www.kurmix.org   _      
# @author    Andree Ochoa <andlody@hotmail.com>     | |/ /   _ _ __ _ __ ___ (_)_  __
# @copyright 2017-2018 Andree Ochoa                 | ' / | | | '__| '_ ` _ \| \ \/ /
# @license   The MIT license                        | . \ |_| | |  | | | | | | |>  < 
# @version   1.0.0                                  |_|\_\__,_|_|  |_| |_| |_|_/_/\_\

from .ReqRes import ReqRes 

class Controller:
	def __init__(self,reqres,view=''):
		self.reqres=reqres
		if reqres == 0:
			self.reqres=ReqRes()
			self.reqres.setView(view)
			self.reqres.setTemplate('default')

	def start(self):
		pass
	def before(self):
		pass
	def after(self):
		pass
	def finish(self):
		pass
	
	def getReqRes(self):
		return self.reqres

	def setKurmix(self,value=None):
		if value==None:
			return self.reqres.getWrite()
		else:
			return self.reqres.error(value)

	def write(self,value):
		self.reqres.setWrite(value)

	def view(self,value):
		self.reqres.setView(value)

	def template(self,value):
		self.reqres.setTemplate(value)

	def show(self):
		self.reqres.show()

	def set(self,index):
		pass