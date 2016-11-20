import urllib
import re

urls = ['http://google.com',
	'http://nytimes.com',
	'http://detik.com',
	'http://lpse.acehtengahkab.go.id/eproc/lelang'
]
i = 0
regex = '<title>(.+?)</title>'
#regex = 'td'
pattern = re.compile(regex)

while i < len(urls):
	htmlFile = urllib.urlopen(urls[i])
	htmlText = htmlFile.read()
	titles = re.findall(pattern, htmlText)
	print titles #htmlText
	print ('===================\n==============\n=========')
	i += 1
