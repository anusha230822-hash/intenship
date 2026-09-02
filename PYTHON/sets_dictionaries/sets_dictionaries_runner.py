def run(level, question):
    fruits = {"Apple", "Banana", "Mango", "Orange", "Grapes"}
    numbers = {10, 20, 30, 40, 50}
    first = {1, 2, 3, 4}; second = {3, 4, 5, 6}
    students = {"Anusha", "Rahul", "Priya", "Neha"}
    marks = {"Anusha": 88, "Rahul": 76, "Priya": 91, "Neha": 65, "Arjun": 82}
    if level == 1:
        results = [fruits, len(numbers), numbers | {60}, numbers | {60, 70}, {1, 2, 3} - {2}, {1, 2, 3} - {2}, {1, 2, 3}.pop(), 30 in numbers, first | second, first & second, first - second, first ^ second, {1, 2}.issubset(first), first.issuperset({1, 2}), set([1, 2, 2, 3, 3])]
    elif level == 2:
        results = [{x for x in numbers if x % 2 == 0}, {x for x in numbers if x % 2}, {"Anusha", "Rahul"} & {"Rahul", "Priya"}, {"Anusha", "Rahul"} - {"Rahul", "Priya"}, {1, 2, 3} | {3, 4, 5}, 50, 10, set(["Anusha", "Anusha", "Rahul"]), {"Anusha", "Rahul"} & {"Rahul", "Priya"}, {"Anusha", "Rahul"} ^ {"Rahul", "Priya"}]
    elif level == 3:
        products = {"Laptop": 55000, "Phone": 30000, "Mouse": 800, "Keyboard": 1500, "Tablet": 25000}
        results = [marks.values(), marks["Anusha"], {"name": "Anusha", "course": "Python"}, {**marks, "Anusha": 95}, {"name": "Anusha", "age": 21}.pop("age"), {"a": 1, "b": 2}.popitem(), marks.keys(), marks.values(), marks.items(), "Anusha" in marks, {k: v for k, v in products.items() if v > 1000}, max(marks, key=marks.get), sum(marks.values()) / len(marks), {x: x*x for x in range(1, 6)}, {x: x**3 for x in range(1, 11)}]
    elif level == 4:
        words = "python makes python learning easy"; values = {"a": 2, "b": 3, "c": 4}
        results = [{k: v for k, v in marks.items() if v > 75}, {"even": len([v for v in values.values() if v % 2 == 0]), "odd": len([v for v in values.values() if v % 2])}, {"Anusha": 75000}, {"Laptop": 5}, sum(values.values()), "meaning of Python", ("Anusha", 65), {c: words.count(c) for c in set(words)}, {w: words.split().count(w) for w in set(words.split())}, dict(zip(["a", "b"], [1, 2]))]
    else:
        results = [{name: "Python" for name in {"Anusha", "Rahul"} | {"Priya"}}, {name: ["Anusha", "Anusha", "Rahul"].count(name) for name in set(["Anusha", "Anusha", "Rahul"])}, {"Anusha": "IT", "Rahul": "HR"}, {"Anusha", "Rahul"}, {"Laptop", "Phone"}]
    print(results[question - 1])
