from PIL import Image
import imagehash
import distance
#hash = imagehash.average_hash(Image.open('fjords.jpg'))
#print(hash)

hash1 = imagehash.average_hash(Image.open('password.jpg'))
string1 = str(hash1)

hash2 = imagehash.average_hash(Image.open('./password/password.jpg'))
string2 = str(hash2)

print distance.hamming(string1, string2)
