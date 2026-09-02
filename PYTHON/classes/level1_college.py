class College:
    def __init__(self, name, location, course):
        self.name = name
        self.location = location
        self.course = course

if __name__ == '__main__':
    c1 = College('Alpha','CityA','CS')
    c2 = College('Beta','CityB','EE')
    c3 = College('Gamma','CityC','ME')
    print(c1.name, c1.location, c1.course)
    print(c2.name, c2.location, c2.course)
    print(c3.name, c3.location, c3.course)
