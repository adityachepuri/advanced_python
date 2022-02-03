import re
s=input('Enter pattern to check:')
m=re.match(s,'bcdefgh')
if m!=None:
    print('Match is avaialble at the beginning of the string')
    print('start index:{} and End index:{}'.format(m.start(),m.end()))
else:
    print('Match is not available at the beginning of the string')

print()
