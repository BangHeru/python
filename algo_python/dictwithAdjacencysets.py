n=[
	'a': set{'bcdef'},
	'b': set{'ce'}, 
	'c': set{'d'}, 
	'd': set{'e'}, 
	'e': set{'f'}, 
	'f': set{'cgh'}, 
	'g': set{'fh'}, 
	'h': set{'fg'}
]

for y in list(n):
	for x in n[y]:
		print(y, ' -- ', x)
