import re
s=input('Enter Registration number:')
m=re.fullmatch('TS[0-3][0-9][A-Z]{2}\d{4}',s)
if m!=None:
    print('Valid Registration Number')
else:
    print('Invalid Registration number')
    
