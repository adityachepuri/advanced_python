import re
s=input('Enter a string:')
m=re.search(s,'abaabaaab')
if m!=None:
    print('Match is available')
    print('First occurence with start index:{} and end index:{}'.format(m.start(),m.end()))
else:
    print('Full string not matched')
          
