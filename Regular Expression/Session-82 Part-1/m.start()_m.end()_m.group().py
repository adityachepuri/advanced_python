import re
count=0
pattern=re.compile('ab')
matcher=pattern.finditer('abaababa')
for m in matcher:
    count=count+1
    print('start:{},end:{},group:{}'.format(m.start(),m.end(),m.group()))
print('The number of occurences:',count)

print()

import re
count=0
matcher=re.finditer('ab','abaababa')
for m in matcher:
    count=count+1
    print('start:{},end:{},group:{}'.format(m.start(),m.end(),m.group()))
print('The number of occurences:',count)
