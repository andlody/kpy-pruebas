# =======  Kurmix  =======                           _  __   www.kurmix.org   _      
# @author    Andree Ochoa <andlody@hotmail.com>     | |/ /   _ _ __ _ __ ___ (_)_  __
# @copyright 2017-2018 Andree Ochoa                 | ' / | | | '__| '_ ` _ \| \ \/ /
# @license   The MIT license                        | . \ |_| | |  | | | | | | |>  < 
# @version   1.0.0                                  |_|\_\__,_|_|  |_| |_| |_|_/_/\_\

from werkzeug import *
import os 
PATH = os.getcwd()

class Router:
	def __init__(self):
		print 'holi'
		self = SharedDataMiddleware(self, {'/public/': os.path.join(PATH, 'public')})
		port = 5000 #os.environ.get('PORT', 8000)
		print '::::::...>>>'+str(port) 
		run_simple('127.0.0.1',port,self, use_reloader=True)

	def __call__(self,environ,start_response):
		return self.route(environ,start_response)
		
	def route(self,environ,start_response):
		request = Request(environ)
		k = request.args.get('k','')
		controller='index'
		action='index'
		
		a=''
		if(k!=''):			
			a = k.split('/')
			controller=a[0]
			if(len(a)>1):
				action=a[1]

		from app.controller.index_controller import *
		index_obj = index_controller(0,controller+'/'+action)
		index_obj.start()

		start_response('200 OK', [('Content-Type', 'text/html')])

		if controller != 'index':
			reqres = index_obj.getReqRes()
			if os.path.isfile(PATH+'/app/controller/'+controller+'_controller.py') :
				exec('from app.controller.'+controller+'_controller import *')
				exec('controller_obj = '+controller+'_controller(reqres)')
			else:			
				return index_obj.setKurmix([100,k,''])
		else:
			controller_obj = index_obj
		
		if not hasattr(controller_obj, action):
			return index_obj.setKurmix([101,action,controller])
			
		exec('action_func = controller_obj.'+action)
		
		import inspect
		n = len(inspect.getargspec(action_func).args)-1
		
		parms = '('
		for i in range(0,n):
			if (i+2) < len(a):
				parms += '"'+str(a[i+2])+'"'
			else:
				parms += '""'

			if (i+1) < n :
				parms+=',';

		parms+=')'
		
		controller_obj.before()

		exec('action_func'+parms)

		controller_obj.after()

		index_obj.finish()

		controller_obj.show()

		return controller_obj.setKurmix()
		
