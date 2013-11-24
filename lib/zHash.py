#!/usr/bin/python

import crypt
import bcrypt
import hashlib
import optparse
from threading import Thread

class Unhash:
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

	def doMD5(self, cryptPass, cryptUser, cryptDict):
	        salt = cryptPass.split('$')[2]
	        test = "$1$"+salt+"$"
	        dictFile = open(cryptDict,'r')
	        for word in dictFile.readlines():
	                word = word.strip('\n')
	                cryptWord = crypt.crypt(word,test)
	                if (cryptWord == cryptPass):
	                        print "[+] Found Password: " + word + " , For User: " + cryptUser + "\r"
	                        return
	        print "[-] Password Not Found for " + cryptUser + "\r"
	        return

	def doSHA256(self, cryptPass, cryptUser, cryptDict):
	        salt = cryptPass.split('$')[2]
	        test = "$5$"+salt+"$"
	        dictFile = open(cryptDict,'r')
	        for word in dictFile.readlines():
	                word = word.strip('\n')
	                cryptWord = crypt.crypt(word,test)
	                if (cryptWord == cryptPass):
	                        print "[+] Found Password: " + word + " , For User: " + cryptUser + "\r"
	                        return
        	print "[-] Password Not Found for " + cryptUser + "\r"
	        return


	def doSHA512(self, cryptPass, cryptUser, cryptDict):
		salt = cryptPass.split('$')[2]
		test = "$6$"+salt+"$"
		dictFile = open(cryptDict,'r')
		for word in dictFile.readlines():
			word = word.strip('\n')
			cryptWord = crypt.crypt(word,test)
			if (cryptWord == cryptPass):
				print "[+] Found Password: " + word + " , For User: " + cryptUser + "\r"
				return
		print "[-] Password Not Found for " + cryptUser + "\r"
		return

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


	def checkMe(self, cryptFile, cryptDict, cryptAlg):
	        passFile = open(cryptFile)
        	for line in passFile.readlines():
	                if ":" in line:
                        	user = line.split(':')[0]
        	                print "[*] " + user + ""
                	        cryptPass = line.split(':')[1].strip(' ')

				if (cryptAlg == 'sha512'):
					print " (SHA-512)"
	        	                t = Thread(target=doSHA512, args=(cryptPass,user,cryptDict))
        		                t.start()
				if (cryptAlg == 'des'):
					t = Thread(target=doDES, args=(cryptPass,user,cryptDict))
					t.start()
				if (cryptAlg == 'md5'):
					t = Thread(target=doMD5, args=(cryptPass,user,cryptDict))
					t.start()
				if (cryptAlg == 'sha256'):
					t = Thread(target=doSHA256, args=(cryptPass,user,cryptDict))
					t.start()
	                        if (cryptAlg == 'blowfish'):
	                                t = Thread(target=doBF, args=(cryptPass,user,cryptDict))
	                                t.start()
				if (cryptAlg == 'auto'):
					#do something


def main():
	parser = optparse.OptionParser("%prog -H <hash file> -D <dict file> -A <algorithm>")
	parser.add_option('-H', dest='myHash', type='string', help='Specify hash file')
	parser.add_option('-D', dest='myDict', type='string', help='Specify dictionary file')
	parser.add_option('-A', dest='myAlgo', type='string', help='Specify algorithm: des, md5, sha256, sha512, blowfish')
	(options, args) = parser.parse_args()
	cryptHash = options.myHash
	cryptDict = options.myDict
	cryptAlgo = options.myAlgo
	if (cryptHash == None) | (cryptDict == None) | (cryptAlgo == None):
		print '[-] You are missing arguments please run with --help option'
		exit(0)
	checkMe(cryptHash, cryptDict, cryptAlgo)

if __name__ == "__main__":
	main()
