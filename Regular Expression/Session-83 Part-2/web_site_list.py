import re
f1=open('websitelist.txt','r')
f2=open('output2.txt','w')
for line in f1:
    list = re.findall('[a-zA-Z]*[\.][a-z]*',line)
    for number in list:
        f2.write(number+'\n')
print('Extracted all the mobile numbers into output.txt')
f1.close()
f2.close()

