class Movie:
    def __init__(self, title, director, year, duration):
        self.title = title
        self.director = director
        self.year = year
        self.duration = duration  # minutes

    def display(self):
        print(f"{self.title} ({self.year}) - Directed by {self.director}, Duration: {self.duration} min")

if __name__ == '__main__':
    m = Movie('Inception', 'Christopher Nolan', 2010, 148)
    m.display()
