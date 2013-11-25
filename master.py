#!/usr/bin/python

import optparse as theparser
from lib.checkhash import *

def main():
	parser = theparser.OptionParser("%prog stuff")
	parser.add_option('-E', dest='myEngi', type='string', help='please see README')
	parser.add_option('-D', dest='myDict', type='string', help='dictionary file')
	parser.add_option('-T', dest='myTarg', type='string', help='the target file for input')
	(options, args) = parser.parse_args()

	myEngi = options.myEngi
	myDict = options.myDict
	myTarg = options.myTarg

	if (myEngi == 'unhash'):
		x = Unhash().checkMe(myTarg, myDict)


if __name__ == '__main__':
	main()
