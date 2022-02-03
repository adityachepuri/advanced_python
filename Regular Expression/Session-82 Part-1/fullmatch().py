import re
s=input('Enter the pattern to check:')
m=re.fullmatch(s,'abcdefgh')
if m!=None:
    print('Full string matched')
else:
    print('Full string not matched')
