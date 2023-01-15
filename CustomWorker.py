import time 
from threading import Thread , active_count

class CustomWorker():
	def __init__(self):
		#super().__init__()
		self.stopped = False 
		self.counter = 4
		self.active=active_count()
		
	def run(self):
		while self.counter != 0:
			if(self.active!=4):
				self.counter=self.active
				self.active=active_count()
				#print(self.counter)
				print(self.active," threads are active right now and ,",(4-self.active)," threads failed")
				time.sleep(2)
				continue
			self.active=active_count()
			self.counter=self.active
				
