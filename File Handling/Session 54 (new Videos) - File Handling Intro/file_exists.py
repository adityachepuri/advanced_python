import os
fname=input('Enter file name:')
if os.path.isfile(fname):
    print('File Exists:',fname)
    f=open(fname,'r')
else:
    print('{} does not exist:'.format(fname))
    sys.exit(0)
print('THe content of the file is:')
data=f.read()
print(data)
