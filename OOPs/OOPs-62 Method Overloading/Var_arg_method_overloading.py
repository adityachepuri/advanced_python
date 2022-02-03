class Test:
    def sum(self,*a):
        total=0
        for x in a:
            total=total+x
        print('The sum:',total)
t=Test()
t.sum()
t.sum(10,20,30,40)
