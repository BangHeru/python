message = raw_input("Enter message to encode: ")
decode = ""

print "Decoded string (in ASCII):"
for ch in message:
   decode += str(int(ord(ch)+12))
   decode += " "
   print ord(ch),
print "\n\n"

print(decode)

decodedMessage = ""

for item in decode.split():
   decodedMessage += chr(int(item))   

print "Chiper Text:", decodedMessage
print "Real Text:", message
