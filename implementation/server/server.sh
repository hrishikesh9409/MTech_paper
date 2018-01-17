#!/bin/bash

#decrypt the client encrypted file
python2 AES.py
#untar the compressed file
tar -xzf client.tar.gz

###VERIFY SIGNATURE#####
openssl base64 -d -in SIGNATURE -out /tmp/sign.sha256
output=`openssl dgst -sha256 -verify public.pem -signature /tmp/sign.sha256 password.jpg`
echo $output

if [[ $output == "Verified OK" ]]; then
	echo "Verification Success!!"

	##Compute server side average hash of the image
	python2 ./password/Average_Hash.py
	echo "Computing Server side Average_Hash"

	#compute the hamming distance of both the client and the server side images
	hd=`python2 Hamming_Distance.py`
	if [[ $hd -lt 11 ]]; then
		echo "Hamming Distance under limit"
	else
		echo "Hamming Distace exceeded LIMIT!  AUTHENTICATION FAILED!"
		exit 1
	fi

	#compute server time and compute server and client time differences 
	st=`python2 server_time.py`
	if [[ $st == 0 ]]; then
		echo "server_time failure!" 
		exit 1
	fi 

	#SURF Algorithm for image matching
	im=`python2 Image_Match.py`
	echo $im
	if [[ $im -gt 20 ]]; then
		echo "MATCH!!"
	else
		echo "Images do not match! AUTHENTICATION FAILED!" 
		exit 1
	fi

	#if all steps are passed, authenticate the client 
	echo
	echo "LOGIN AUTHENTICATED!"
	echo

else
	echo -e "Signature Verification Failed! Denied Access!!" 
fi
	exit 1

#echo $output	
