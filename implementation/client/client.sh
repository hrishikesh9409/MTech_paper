#!/bin/bash

#generate AES key
python2 AES_Key_Generator.py
#take a picture of the client with time stamp
python2 Picture.py
#compute the Average Hash of the picture password
python2 Average_Hash.py

#Setup RSA public and private keys
openssl genrsa -aes128 -passout pass:hrishi -out private.pem 4096
openssl rsa -in private.pem -passin pass:hrishi -pubout -out public.pem

#Generate the RSA Signature for the picture password
openssl dgst -sha256 -sign private.pem -out /tmp/sign.sha256 password.jpg
openssl base64 -in /tmp/sign.sha256 -out SIGNATURE

#compress the files together... prepare to encrypt using AES
tar -czf client.tar.gz password.jpg AV_HASH.DAT SIGNATURE TIMESTAMP.DAT public.pem

#encrypt the compressed tar file using AES encryption scheme
python2 AES.py

## for now rudimentary key exchange with the server
cp client.tar.gz.enc AES_KEY.DAT ../server/