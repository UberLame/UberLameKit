#!/usr/bin/python

import crypt
import bcrypt
import hashlib
import optparse
from threading import Thread

class zBF:
        def doBF(self, cryptPass, cryptUser, cryptDict):
                xtype = cryptPass.split('$')[1]
                rounds = cryptPass.split('$')[2]
                odd = cryptPass.split('$')[3]
                test = "$" + xtype + "$" + rounds + "$"
                dictFile = open(cryptDict,'r')
                for word in dictFile.readlines():
                        word = word.strip('\n')
                        kryptWord = test + odd[0:22] + "$"
                        #kryptWord = test + hashlib.sha1(word).hexdigest()[0:22] + "$"
                        cryptWord = bcrypt.hashpw(word,kryptWord)
                        if (cryptWord == cryptPass):
                                print "[+] Found Password: " + word + " , For User: " + cryptUser + "\r"
                                return
                print "[-] Password Not Found for " + cryptUser + "\r"
                return

	def checkMe(self, cryptPass, cryptUser, cryptDict):
		t = Thread(target=self.doBF, args=(cryptPass,cryptUser,cryptDict))
		t.start()

def main():
	exit(0)

if __name__ == "__main__":
	main()
