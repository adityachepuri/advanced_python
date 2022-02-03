import re
matcher=re.finditer('\d','a7bk9z6')
for m in matcher:
    print(m.start(),'---',m.end(),'----',m.group())
print()
import re
matcher=re.finditer('\D','a7bk9z6')
for m in matcher:
    print(m.start(),'---',m.end(),'----',m.group())
