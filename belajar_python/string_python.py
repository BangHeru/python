str = 'Hello World!'
count = 0
panjang = len(str)

print (str)
print (str[0])
print (str[2:5])
print (str[2:])
print (str * 2)
print (str + "TEST")
print (len(str))


while (count < len(str)):
	print (str[0:count])
	count = count + 1

while (count > 0):
	print (str[0:count])
	count = count - 1

