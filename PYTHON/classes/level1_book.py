class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

if __name__ == '__main__':
    b1 = Book('Book A','Author X',100)
    b2 = Book('Book B','Author Y',150)
    print(b1.title, b1.author, b1.price)
    print(b2.title, b2.author, b2.price)
