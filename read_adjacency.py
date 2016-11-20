# Open a file
fo = open("adjacency.txt", "r+")
str = fo.read();
graph = {}
graph.update(str)
#print "Read String is : ", str
print graph
# Close opend file
fo.close()
