from zipfile import*
f=ZipFile('files.zip','w',ZIP_DEFLATED)
f.write('Cricket.txt')
f.write('Heroes.txt')
f.write('Movies.txt')
f.close
print('files.zip file created successfully')
