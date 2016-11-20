import random

list1 = [20, 16, 10, 5];
list2 = ['A','B','C','D'];
list3 = list1 + list2

random.shuffle(list1)
print ("Reshuffled list : ",  list1)

random.shuffle(list2)
print ("Reshuffled list : ",  list2)

count = 0

while (count < len(list3)):
	random.shuffle(list3)
	print ("Acak ke : ", count + 1, " ", list3)
	count = count + 1

for x in list3:
	print (x)

