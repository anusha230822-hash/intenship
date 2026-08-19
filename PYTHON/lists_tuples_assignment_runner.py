def run(group, question):
    numbers = [40, 10, 30, 20, 50, 60, 70, 80, 90, 100]
    names = ["Anusha", "Rahul", "Priya", "Neha"]
    if group == 1:
        results = [
            ["Apple", "Banana", "Mango", "Orange", "Grapes"],
            ([1, 2, 3, 4, 5][0], [1, 2, 3, 4, 5][-1]),
            numbers[:5], numbers[-5:], len(names), numbers + [110],
            ["Anusha", "Rahul", "Priya"], [1, 99, 3], [1, 2, 3, 4][:-1], sorted(numbers),
            sorted(numbers, reverse=True), numbers[::-1], "Priya" in names, [1, 2, 2, 3].count(2), numbers.index(30),
        ]
        print(results[question - 1])
    elif group == 2:
        even = [x for x in numbers if x % 2 == 0]
        odd = [x for x in numbers if x % 2]
        total = 0
        for value in numbers: total += value
        largest = numbers[0]
        smallest = numbers[0]
        for value in numbers[1:]:
            if value > largest: largest = value
            if value < smallest: smallest = value
        results = [even, odd, total, largest, smallest, total / len(numbers), len([x for x in numbers if x > 50]), (even, odd), list(dict.fromkeys([1, 2, 2, 3, 4, 4])), [x*x for x in numbers]]
        print(results[question - 1])
    elif group == 3:
        data = ("red", "blue", "green", "yellow", "black")
        results = [data, (data[0], data[-1]), data[1:4], len((1, 2, 3, 4)), (1, 2, 2, 3).count(2), (1, 2, 3).index(2), (1, 9, 4, 7), ("Anusha", 21, "Python", 88), ("Anusha", 21, "Python", 88), ("old", "new")]
        print(results[question - 1])
    else:
        students = [("Anusha", 88), ("Rahul", 72), ("Priya", 91), ("Neha", 65), ("Arjun", 79)]
        products = [("Laptop", 55000, 2), ("Mouse", 800, 3)]
        employees = [("Anusha", "Developer", 75000), ("Rahul", "Tester", 55000)]
        nested = [["Anusha", 80, 90, 85], ["Rahul", 70, 75, 72]]
        results = [[x for x in students if x[1] > 75], [(name, price * quantity) for name, price, quantity in products], max(employees, key=lambda x: x[2]), [(row[0], sum(row[1:]), sum(row[1:]) / 3) for row in nested], ([1, 2], [3, 4]), tuple([1, 2, 3]), list((1, 2, 3)) + [4, 5, 6], [1, 2] + [3, 4], (1, 2) + (3, 4), next(student for student in students if student[0] == "Priya")]
        print(results[question - 1])
