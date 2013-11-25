#!/usr/bin/python

from lib.brutessh import *

class Bruteforce:
	def checkMe(self, myHost, myUser, myDict, myType):
		if (myType == 'ssh'):
			bSsh().checkMe(myHost, myUser, myDict)
		else:
			print "[E] nothing specified"

def main():
	exit(0)

if __name__ == "__main__":
	main()
