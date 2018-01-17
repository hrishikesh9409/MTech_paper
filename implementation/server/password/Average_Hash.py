from PIL import Image
import imagehash

hash1 = imagehash.average_hash(Image.open('password.jpg'))
#print hash1

with open("AV_HASH.DAT", "w") as text_file:
	text_file.write(str(hash1))
