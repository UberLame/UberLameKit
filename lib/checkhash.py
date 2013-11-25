#!/usr/bin/python

from lib.sha512 import *
from lib.md5 import *
from lib.blowfish import *
from lib.sha256 import *
from lib.des import *

class Unhash:
	def checkMe(self, cryptFile, cryptDict):
		nMd5 = 0
		nSha512 = 0
		nBf = 0
		nSha256 = 0
		nDes = 0

		print "\r[*] Preparing encrypted files for threading\r"
	        passFile = open(cryptFile)
        	for line in passFile.readlines():
	                if ":" in line:
                        	user = line.split(':')[0]
                	        cryptPass = line.split(':')[1].strip(' ')

				if (cryptPass[0:3] == '$6$'):
					nSha512 += 1	
					zSha512().checkMe(cryptPass,user,cryptDict)
				elif (cryptPass[0:3] == '$5$'):
					nSha256 += 1
					zSha256().checkMe(cryptPass,user,cryptDict)
				elif (cryptPass[0:3] == '$1$'):
					nMd5 += 1
					zMd5().checkMe(cryptPass,user,cryptDict)
				elif (cryptPass[0:3] == '$2$') | (cryptPass[0:4] == '$2a$') | (cryptPass[0:4] == '$2x$') | (cryptPass[0:4] == '$2y$'):
					nBf += 1
					zBf().checkMe(cryptPass,user,cryptDict)
				else:
					nDes += 1
					zDes().checkMe(cryptPass,user,cryptDict)


		if (nSha512 > 0):
			print "[*] Found " + str(nSha512) + " - SHA512 hashes"
		if (nMd5 > 0):
			print "[*] Found " + str(nMd5) + " - MD5 hashes"
		if (nBf > 0):
			print "[*] Found " + str(nBf) + " - Blowfish hashes"
		if (nSha256 > 0):
			print "[*] Found " + str(nSha256) + " - SHA256 hashes"
		if (nDes > 0):
			print "[*] Found " + str(nDes) + " - DES hashes"

def main():
	exit(0)

if __name__ == "__main__":
	main()
