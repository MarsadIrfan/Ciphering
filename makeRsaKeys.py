import random, sys, os, rabinMiller, cryptoMath

def main():
	print("Making key files...")
	makeKeyFiles('mm_irfan', 1024)
	print()
	print("Key files made.")
	
def generateKey(keySize):
	print('Generating p prime...')
	p = rabinMiller.generateLargePrime(keySize)
	print('Generating q prime...')
	q = rabinMiller.generateLargePrime(keySize)
	n = p * q
	
	print('Generating e that is relatively prime to (p-1)*(q-1)...')
	while True:
		e = random.randrange(2 ** (keySize - 1), 2 ** (keySize))
		if cryptoMath.gcd(e, (p - 1) * (q - 1)) == 1:
			break
			
	print('Calculating d that is mod inverse of e...')
	d = cryptoMath.findModInverse(e, (p - 1) * (q - 1))
	
	publicKey = (n, e)
	privateKey = (n, d)
	
	print('Public key:', publicKey)
	print('Private key:', privateKey)
	
	return (publicKey, privateKey)

	
def makeKeyFiles(name, keySize):
	
	if os.path.exists('%s_pubkey.txt' % (name)) or os.path.exists("%s_privkey.txt" % (name)):
		sys.exit("WARNING: The file %s_pubkey.txt or %s_privkey.txt already exists! Use a different name or delete these files and re-run this program." % (name, name))
		
	publicKey, privateKey = generateKey(keySize)
	
	print()
	
	print("The public key is a %s and a %s digit number." % (len(str(publicKey[0])), len(str(publicKey[1]))))
	print("Writing public key to file %s_pubkey.txt...." % (name))
	fo = open("%s_pubkey.txt" % (name), 'w')
	fo.write('%s,%s,%s' % (keySize, publicKey[0], publicKey[1]))
	fo.close()
	
	print()
	print("The private key is a %s and a %s digit number." % (len(str(publicKey[0])), len(str(publicKey[1]))))
	print("Writing private key to file %s_privkey.txt...." % (name))
	fo = open("%s_privkey.txt" % (name), 'w')
	fo.write("%s,%s,%s" % (keySize, privateKey[0], privateKey[1]))
	fo.close()
	
if __name__ == "__main__":
	main()


	
