price = 33.3
TotalAmount = 50
with open("t.txt", "w") as text_file:
	text_file.write(str(price))

file = open('AV_HASH.DAT', 'r')
n = file.readline()

print n