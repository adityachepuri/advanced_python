import re
s=input('Enter a mailid for validation:')
m=re.fullmatch('\w[a-zA-Z0-9_.]*@[a-z0-9]+[.][a-z]*',s)
# m=re.fullmatch('\w[a-zA-Z0-9_.]*@[gmail|rediff]+[.][a-z]*',s)
if m!=None:
    print('Valid Mail Id')
else:
    print('Invalid Mail Id')
