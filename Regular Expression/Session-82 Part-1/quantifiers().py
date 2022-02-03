print('Prints exactly one "a" (even if there are more "a"s it prints the first occurence)')
import re
matcher=re.finditer('[a]','a7aaab @ Kaaa9aaZ')
for m in matcher:
    print(m.start(),'......',m.group())

print()

print('Prints atleast one "a"')
import re
matcher=re.finditer('[a+]','a7aaab @ Kaaa9aaZ')
for m in matcher:
    print(m.start(),'......',m.group())

print()

print('Prints any number of "a"s including zero also')
import re
matcher=re.finditer('[a*]','a7aaab @ Kaaa9aaZ')
for m in matcher:
    print(m.start(),'......',m.group())

print()

print('[a?] Prints atmost one "a" or zero or more noof "a"s')
import re
matcher=re.finditer('[a?]','a7aaab @ Kaaa9aaZ')
for m in matcher:
    print(m.start(),'......',m.group())

print()

#---------------------Need to remodify the program -------------------------#

print('a{n} Prints exactly "n" no.of "a"s')
import re
matcher=re.finditer('[a{n}]','a7aaab @ Kaaa9aaZ')
for m in matcher:
    print(m.start(),'......',m.group())

print()

print('a{m,n} Prints exactly "n" no.of "a"s')
import re
matcher=re.finditer('[a{1,3}]','a7aaab @ Kaaa9aaZ')
print("Total no.of a's in the string are:",matcher)
print()
