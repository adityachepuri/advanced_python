f1=open("newpic.jpg",'rb')
f2=open('newpic2.jpg','wb')
bytes=f1.read()
f2.write(bytes)
print('New image is available with name:newpic.jpg')
f2.close()
