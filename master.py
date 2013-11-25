#!/usr/bin/python

import optparse as theparser
from eng.checkhash import *
from eng.checkbrute import *

def main():
	parser = theparser.OptionParser("%prog stuff")
	parser.add_option('-E', dest='myEngi', type='string', help='please see README')
	parser.add_option('-D', dest='myDict', type='string', help='dictionary file')
	parser.add_option('-T', dest='myTarg', type='string', help='the target file for input')
	parser.add_option('-U', dest='myUser', type='string', help='the target username')
	parser.add_option('-H', dest='myHost', type='string', help='the target hostname or ipaddress')
	parser.add_option('-A', dest='myType', type='string', help='the attack type for the engine \(if required\)')
	(options, args) = parser.parse_args()

	myEngi = options.myEngi
	myDict = options.myDict
	myTarg = options.myTarg
	myUser = options.myUser
	myHost = options.myHost
	myType = options.myType

	if (myEngi == 'unhash'):
		x = Unhash().checkMe(myTarg, myDict)
	elif (myEngi == 'bruteforce'):
		x = Bruteforce().checkMe(myHost, myUser, myDict, myType)
	else:
		print "[E] please read the README file for more help"


if __name__ == '__main__':
	main()
