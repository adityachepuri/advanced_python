import os,sys
fname=input('Enter File Name:')
if os.path.isfile(fname):
    print('File exists:',fname)
    f=open(fname,'r')
else:
    print('File does not exist:',fname)
    sys.exit(0)
lcount=wcount=ccount=0
for line in f:
    lcount=lcount+1
    ccount=ccount+len(line)
    words=line.split()
    wcount=wcount+len(words)
print('The number of lines"',lcount)
print('The number of words:',wcount)
print('The number of charecters:',ccount)

print()
f=open(fname,'r')
data=f.read()
print(data)
