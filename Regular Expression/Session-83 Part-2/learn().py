import re
s="Learning Python is very easy"
res=re.search('^Tearn',s)
if res!=None:
    print('Target starts with Learn')
else:
    print('Target string does not start with Learn')
print(res)
