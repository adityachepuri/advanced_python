f=open('aditya1.txt','w')
f.write('Aditya\n')
print()
f.write('Software\n')
print()
f.write('Solutions\n')
print()
print('Data written successfully')



f=open('aditya1.txt','r')
data=f.read()
print(data)
print(type(data))
f.close()

f=open('aditya1.txt','r')
data=f.read(10)
print(data)
f.close()

print()

f=open('aditya1.txt','r')
print(f.readline(),end=' ')
print(f.readline(),end=' ')
print(f.readline(),end=' ')
f.close()

print()

f=open('aditya1.txt','r')
list=f.readlines()
print(list)
f.close()
print()

## For printing total data using for loop ##
f=open('aditya1.txt','r')
list=f.readlines()
for lines in list:
    print(lines,end=' ')
f.close()
