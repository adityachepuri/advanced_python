class Movie:
    def info(self):
        print('Movie Name:',self.name)
        print('Hero Name:',self.hero)
        print('Heroine Name:',self.heroine)
        print('Movie Rating:',self.rating)
        print()

m=Movie()
m.name='bahubali'
m.hero='Prabhas'
m.heroine='Anushka'
m.rating=30

m.info()
print(m.__dict__)
