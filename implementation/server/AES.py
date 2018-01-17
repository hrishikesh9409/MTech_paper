import os, random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
 
def decrypt(key, filename):
        chunk_size = 64*1024
        output_file = filename[:-4]
        with open(filename, 'rb') as inf:
            filesize = long(inf.read(16))
            IV = inf.read(16)
            decryptor = AES.new(key, AES.MODE_CBC, IV)
            with open(output_file, 'wb') as outf:
                while True:
                    chunk = inf.read(chunk_size)
                    if len(chunk)==0:
                        break
                    outf.write(decryptor.decrypt(chunk))
                outf.truncate(filesize)
 
def getKey(password):
    hasher = SHA256.new(password)
    return hasher.digest()
 
def main():

	filename = 'client.tar.gz.enc'
	
	file = open('AES_KEY.DAT', 'r')
	password = file.readline()

	decrypt(getKey(password), filename)
	#print "Done\n%s ==> %s"%(filename, filename[:-4])
 
if __name__ == "__main__":
    main()