import urllib
import re

urls = ['http://lpse.acehtengahkab.go.id/eproc/lelang']
i = 0
regex = '<tbody>(.+?)</tbody>'
#regex = 'td'
pattern = re.compile(regex)

while i < len(urls):
	htmlFile = urllib.urlopen(urls[i])
	htmlText = htmlFile.read()
	titles = re.findall(pattern, htmlText)
	print titles #htmlText
	print ('===================\n==============\n=========')
	i += 1