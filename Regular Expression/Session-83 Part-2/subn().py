import re
s=re.subn('\w','*','a1w5b8b7*^$')
print(s[0])
print(s[1])


import re
s=re.subn('\W','*','a1w5b8b7*^$')
print(s[0])
print(s[1])

