class P:
    def property(self):
        print('land + cash + gold + power')

    def marriage(self):
        print('Appalamma | Subbalaxmi')

class C(P):
    def marriage(self):
        super().marriage()
        print('Sunny | Subbalaxmi')

c=C()
c.property()
c.marriage()
