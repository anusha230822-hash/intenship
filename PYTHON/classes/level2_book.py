class Book:
    def __init__(self, title, author, price, pages):
        self.title = title
        self.author = author
        self.price = price
        self.pages = pages

if __name__ == '__main__':
    books = [
        Book('B1','A1',200,250),
        Book('B2','A2',150,200),
        Book('B3','A3',300,400),
    ]
    for b in books:
        print(b.title, b.author, b.price, b.pages)
