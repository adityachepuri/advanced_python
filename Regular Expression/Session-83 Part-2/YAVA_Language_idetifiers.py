import re
s=input('Enter identifier to validate')
m=re.fullmatch('[a-k][0369][a-zA-Z0-9#]*',s)
if m!=None:
    print(s,'is valid Yava identifier')
else:
    print(s,'is not valid identifier')
