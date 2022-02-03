class Movie:
    def vd(self,name,hero,heroine,rating):
        self.name=name
        self.hero=hero
        self.heroine=heroine
        self.rating=rating

    def info(self):
        print('Movie Name:',self.name)
        print('Hero Name:',self.hero)
        print('Heroine Name:',self.heroine)
        print('Movie Rating:',self.rating)
        print()

m=Movie()
m.vd('Spider','Mahesh','Anushka',30)
m.info()
