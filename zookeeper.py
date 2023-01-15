from socket import *
from socket import error as SocketError
from broker_check import *
from broker_check import _getOfflineBrokers
from template import Template
from broker import *
#from broker import handleSender
from threading import Thread, Lock, active_count
import threading
import traceback
import json
from utils import handleForceExit
from random import randint
import time 
from CustomWorker import CustomWorker


class zookeeper(Template):

	def __init__(self):
		super(zookeeper , self).__init__()
		self.leader = None 
		self.lock = Lock()
		print("hello")
		self.socket.connect((self.serverIP,self.serverPort))
		print("hello")
		self.log(f'Zookeeper started at {self.serverIP}:{self.serverPort}')
		
	def f1(self):
        	self.log("hi")
		
	def checkBroker(self):
		self.lock.acquire()
		self.active= active_count()
		print("Number of active threads" , self.active)
		
		self.leader = threading.enumerate()[0]
		print(self.leader)
		self.status = getBrokerStatus(4,self.active)
		print("The status of the broker is ", self.status)
		
		self.num = _getOfflineBrokers(4,self.active)
		self.t = False 
		while self.active!=0:
				self.leader = threading.enumerate()[0]
				print(self.leader)
				if not self.t:
					#self.t=True
					self.t = CustomWorker()
					self.t.run()
					print("starting")
				if self.t:
					self.t=CustomWorker()
					 
					
		
	def execute(self):
		self.checkBroker()
			
if  __name__ == "__main__":
	handleForceExit(zookeeper)
	

	
