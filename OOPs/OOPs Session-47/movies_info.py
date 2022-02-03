class Movie:
    def __init__(self,name,hero,heroine,rating):
        self.name=name
        self.hero=hero
        self.heroine=heroine
        self.rating=rating
    def info(self):
        print("Movie Name:",self.name)
        print("Hero Name:",self.hero)
        print("Heroine Name:",self.heroine)
        print("Movie Rating:",self.rating)
        print()

movies=[Movie('Bahubali','Prabhas','Anushka',99), #Movie is the class name
        Movie('Spyder','Mahesh Babu','Rakul',25),
        Movie('Rayees','Sharukh','Sunny',50)]
for movie in movies:  # in place of movie we can use even x/y/z or any variable
    movie.info()
        
