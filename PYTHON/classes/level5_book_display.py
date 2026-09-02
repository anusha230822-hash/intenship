class Book:
    def __init__(self, title, author, pages, publisher=None):
        self.title = title
        self.author = author
        self.pages = pages
        self.publisher = publisher

    def display_info(self):
        print(f"Title: {self.title}\nAuthor: {self.author}\nPages: {self.pages}")
        if self.publisher:
            print('Publisher:', self.publisher)

if __name__ == '__main__':
    b = Book('The Alchemist', 'Paulo Coelho', 208, 'HarperOne')
    b.display_info()
