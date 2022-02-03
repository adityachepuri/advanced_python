print('  ------------ PREDEFINED CHARECTER CLASSES -------------')
print()
print('\s counts space charecter')
import re
matcher=re.finditer('\s','a7b @ K9Z')
for m in matcher:
    print(m.start(),'.....', m.group())

print()
print('\S counts everything except space charecter')
import re
matcher=re.finditer('\S','a7b @ K9Z')
for m in matcher:
    print(m.start(),'.....', m.group())

print()
print('\d counts [0-9] digits')
import re
matcher=re.finditer('\d','a7b @ K9Z')
for m in matcher:
    print(m.start(),'.....', m.group())

print()
print('\D counts evrything except [0-9] digits')
import re
matcher=re.finditer('\D','a7b @ K9Z')
for m in matcher:
    print(m.start(),'.....', m.group())

print()
print('\w counts any word charecter a-z, A-Z, 0-9')
import re
matcher=re.finditer('\w','a7b @ K9Z')
for m in matcher:
    print(m.start(),'.....', m.group())

print()

print('\W counts special charecters (charecters except a-z, A-Z, 0-9)')
import re
matcher=re.finditer('\W','a7b @ K9Z')
for m in matcher:
    print(m.start(),'.....', m.group())

print()
print('. counts all charecters alphabets, digits, special charecters & Total no.of charecters')
count=0
import re
matcher=re.finditer('.','a7b @ K9Z')
for m in matcher:
    count=count+1
    print(m.start(),'.....', m.group())
print('Total length of string is:',count)

