class Movie:
    def __init__(self, name, hero, heroine, rating):
        self.name = name
        self.hero = hero
        self.heroine = heroine
        self.rating = rating

if __name__ == '__main__':
    m1 = Movie('FilmA','Hero1','Heroine1',4.5)
    m2 = Movie('FilmB','Hero2','Heroine2',4.0)
    print(m1.name, m1.hero, m1.heroine, m1.rating)
    print(m2.name, m2.hero, m2.heroine, m2.rating)
