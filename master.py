#!/usr/bin/python

import optparse as theparser
from lib.Zombie import *

def main():
	parser = theparser.OptionParser("%prog stuff")
	parser.add_option('-L', dest='myFile', type='string', help='bot file')
	(options, args) = parser.parse_args()
	myFile = options.myFile

	x = Zombie().woot(myFile)

if __name__ == '__main__':
	main()
