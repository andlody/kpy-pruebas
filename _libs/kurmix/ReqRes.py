# =======  Kurmix  =======                           _  __   www.kurmix.org   _      
# @author    Andree Ochoa <andlody@hotmail.com>     | |/ /   _ _ __ _ __ ___ (_)_  __
# @copyright 2017-2018 Andree Ochoa                 | ' / | | | '__| '_ ` _ \| \ \/ /
# @license   The MIT license                        | . \ |_| | |  | | | | | | |>  < 
# @version   1.0.0                                  |_|\_\__,_|_|  |_| |_| |_|_/_/\_\

class ReqRes:
	def __init__(self):
		self.text_write= ''
		self.bnd_write = False

	def setWrite(self,value):
		self.bnd_write = True
		self.text_write +=value

	def getWrite(self):
		return self.text_write

	def setView(self,value):
		self.view = value

	def show(self):
		if self.bnd_write:
			return

		import os
		from jinja2 import Environment, FileSystemLoader
		from .Views import Views
		
		PATH = os.getcwd()

		j2_env = Environment(loader=FileSystemLoader(PATH), trim_blocks=True)
		
		if self.template == None:
			if os.path.isfile(PATH+'/app/view/'+self.view+'.html'):
				self.text_write = str(j2_env.get_template('app/view/'+self.view+'.html').render(v=Views(self.view)).encode('utf8'))
			else:
				self.text_write = self.error([402,self.view,''])
		else:
			if os.path.isfile(PATH+'/app/view/_templates/'+self.template+'.html'):
				if os.path.isfile(PATH+'/app/view/'+self.view+'.html'):
					self.text_write = str(j2_env.get_template('app/view/_templates/'+self.template+'.html').render(v=Views(self.view)).encode('utf8'))
				else:
					self.text_write = self.error([402,self.view,''])
			else:
				self.text_write = self.error([401,self.template,''])				

	def setTemplate(self,value):
		self.template = value

	def error(self,v):
		from app._config.Config import Config
		if not Config.DEV:
			return self.error404()

		return {
        	101: str("ERROR: En el Router, no existe la accion:<strong> "+v[1]+" </strong> en el controlador:<strong> "+v[2]+"</strong><br>"),
        	103: str("ERROR: En el Router, no existe el controlador:<strong> "+v[1]+" </strong><br>"),
        	401: str("ERROR: En la vista, Template:<strong> "+v[1]+" </strong> Posiblemente no existe."),
        	402: str("ERROR: En la vista, Al redireccionar:<strong> "+v[1]+" </strong><br> Posiblemente no existe.")
    	}.get(v[0],'ERROR')
 
	def error404(self):
		self.setView("_templates/_404");
		self.setTemplate(None);
		self.show();
		return self.text_write
