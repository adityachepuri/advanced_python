import os
fname=input('Enter file name:')
if os.path.isfile(fname):
    print('File Exists:',fname)
    f=open(fname,'r')
    print('THe content of the file is:')
    data=f.read()
    print(data)
else:
    print('{} does not exist:'.format(fname))
    sys.exit(0)

