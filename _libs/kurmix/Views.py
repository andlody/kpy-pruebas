class Views:
	def __init__(self,value):
		self.body = 'app/view/'+value+'.html'
	
	def partial(self,value):
		return 'app/view/_partials/'+value+'.html'

	def get(self):
		return 'Holi'