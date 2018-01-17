import os, random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
 
def encrypt(key, filename):
    chunk_size = 64*1024
    output_file = filename+".enc"
    file_size = str(os.path.getsize(filename)).zfill(16)
    IV = ''
    for i in range(16):
        IV += chr(random.randint(0, 0xFF))
    encryptor = AES.new(key, AES.MODE_CBC, IV)
    with open(filename, 'rb') as inputfile:
        with open(output_file, 'wb') as outf:
            outf.write(file_size)
            outf.write(IV)
            while True:
                chunk = inputfile.read(chunk_size)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                   chunk += ' '*(16 - len(chunk)%16)
                outf.write(encryptor.encrypt(chunk))
 
def getKey(password):
    hasher = SHA256.new(password)
    return hasher.digest()
 
def main():
	filename = 'client.tar.gz'

	file = open('AES_KEY.DAT', 'r')
	password = file.readline()

	encrypt(getKey(password), filename)
	print "AES Encryption Success!\n%s ==> %s"%(filename, filename+".enc")
 
if __name__ == "__main__":
    main()