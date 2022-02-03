import re,urllib
import urllib.request
u=urllib.request.urlopen("https://www.redbus.in/info/contactus")
text=u.read()
numbers=re.findall('[0-9]{3}[-][0-9]{8}',str(text))
for n in numbers:
    print(n)
