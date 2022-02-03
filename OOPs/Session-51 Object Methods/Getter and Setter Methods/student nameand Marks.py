l=[]
n=int(input('Enter no.of Student:'))
for i in range(n):
      s=Student()
      name=input('Enter name of the student')
      marks=int(input('Enter marks of the student'))
      s.setName(name)
      s.setMarks(marks)
      l.append(s)

for s in l:
    print('Student Name:',s.getName())
    print('Student Marks:',s.getMarks())
    print()
