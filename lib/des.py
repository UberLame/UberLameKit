#!/usr/bin/python

import crypt
import bcrypt
import hashlib
import optparse
from threading import Thread

class zDes:
        def doDES(self, cryptPass, cryptUser, cryptDict):
                salt = cryptPass[0:2]
                dictFile = open(cryptDict,'r')
                for word in dictFile.readlines():
                        word = word.strip('\n')
                        cryptWord = crypt.crypt(word,salt)
                        if (cryptWord == cryptPass):
                                print "[+] Found Password: " + word + " ; For User: " + cryptUser + "\r"
                                return
                print "[-] Password Not Found for " + cryptUser + "\r"
                return

	def checkMe(self, cryptPass, cryptUser, cryptDict):
		t = Thread(target=self.doDES, args=(cryptPass,cryptUser,cryptDict))
		t.start()

def main():
	exit(0)

if __name__ == "__main__":
	main()
