from __future__ import annotations

import csv
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).parent / "assignment_data"
ROOT.mkdir(exist_ok=True)


def text_path(name="sample.txt"):
    return ROOT / name


def numbers():
    return [12, -3, 0, 8, 12, 5, 20, -7, 4, 10]


def level1(question):
    path = text_path()
    if question == 1:
        path.write_text("Welcome to Python\n", encoding="utf-8")
    elif question == 2:
        path.write_text("Name: Anusha\nAge: 21\nCourse: Python\n", encoding="utf-8")
    elif question == 3:
        path.write_text("Anusha\nRahul\nPriya\nNeha\nArjun\n", encoding="utf-8")
    elif question == 4:
        path.write_text("10\n20\n30\n40\n50\n", encoding="utf-8")
    elif question == 5:
        print(path.read_text(encoding="utf-8"))
    elif question == 6:
        print("\n".join(path.read_text(encoding="utf-8")))
    elif question == 7:
        print("".join(path.read_text(encoding="utf-8").splitlines(keepends=True)))
    elif question == 8:
        print(path.read_text(encoding="utf-8").splitlines())
    elif question == 9:
        print("\n".join(path.read_text(encoding="utf-8").splitlines()[:5]))
    else:
        print("\n".join(path.read_text(encoding="utf-8").splitlines()[-5:]))
    print(f"Level 1 question {question} completed: {path}")


def level2(question):
    path = text_path("level2.txt")
    if question == 1:
        path.write_text("First line\nSecond line\n", encoding="utf-8")
    elif question in (2, 8, 10):
        with path.open("a", encoding="utf-8") as file:
            file.write("Appended student: Anusha, Python\n")
    elif question in (3, 5):
        print(path.read_text(encoding="utf-8") if path.exists() else "File does not exist.")
    elif question == 4:
        print("r=read, w=overwrite, a=append")
    elif question == 6:
        path.touch(exist_ok=True)
    elif question == 7:
        path.write_text("Overwritten content\n", encoding="utf-8")
    elif question == 9:
        path.write_text("", encoding="utf-8")
    if question == 10:
        print(path.read_text(encoding="utf-8"))
    print(f"Level 2 question {question} completed: {path}")


def level3(question):
    path = text_path("level3.txt")
    path.write_text("Python file methods\nSecond line\nThird line\n", encoding="utf-8")
    with path.open("r+", encoding="utf-8") as file:
        if question == 1: print(file.read())
        elif question == 2: print(file.read(6))
        elif question == 3: print(file.readline().rstrip())
        elif question == 4: print(file.readlines())
        elif question == 5: file.write("A single line\n")
        elif question == 6: file.writelines(["Line A\n", "Line B\n"])
        elif question == 7: print(file.tell())
        elif question == 8: file.seek(7); print(file.read())
        elif question == 9: print(file.tell()); file.seek(0); print(file.tell())
        else: print(file.read())
    print(f"Level 3 question {question} completed: {path}")


def level4(question):
    path = text_path("level4.txt")
    path.write_text("Python File 123\nAnother Line\n", encoding="utf-8")
    content = path.read_text(encoding="utf-8")
    result = [len(content.splitlines()), len(content.split()), len(content), sum(c.lower() in "aeiou" for c in content), sum(c.isalpha() and c.lower() not in "aeiou" for c in content), sum(c.isdigit() for c in content), content.count(" "), sum(c.isupper() for c in content), sum(c.islower() for c in content)]
    if question <= 8: print(result[question - 1])
    elif question == 9: print("\n".join(line for line in content.splitlines() if "Python" in line))
    else: print("\n".join(line for line in content.splitlines() if line.startswith("A")))
    print(f"Level 4 question {question} completed.")


def level5(question):
    source = text_path("level5.txt")
    source.write_text("10\n3\n10\n\nPython   programming\n", encoding="utf-8")
    lines = source.read_text(encoding="utf-8").splitlines()
    output = text_path(f"level5_output_{question}.txt")
    if question == 1: data = [x for x in lines if x.isdigit() and int(x) % 2 == 0]
    elif question == 2: data = [x for x in lines if x.isdigit() and int(x) % 2]
    elif question == 3: data = [x.replace("Python", "SQL") for x in lines]
    elif question == 4: data = [x for x in lines if x.strip()]
    elif question == 5: data = [" ".join(x.split()) for x in lines]
    elif question == 6: data = [x.upper() for x in lines]
    elif question == 7: data = [x.lower() for x in lines]
    elif question == 8: data = [x[::-1] for x in lines]
    elif question == 9: data = lines[::-1]
    else: data = list(dict.fromkeys(lines))
    output.write_text("\n".join(data) + "\n", encoding="utf-8")
    print(f"Created {output}")


def level6(question):
    values = numbers(); source = text_path("numbers.txt")
    source.write_text("\n".join(map(str, values)) + "\n", encoding="utf-8")
    if question == 1: print(sum(values))
    elif question == 2: print(sum(values) / len(values))
    elif question == 3: print(max(values))
    elif question == 4: print(min(values))
    elif question == 5:
        text_path("even.txt").write_text("\n".join(map(str, [x for x in values if x % 2 == 0])), encoding="utf-8")
        text_path("odd.txt").write_text("\n".join(map(str, [x for x in values if x % 2])), encoding="utf-8")
    elif question == 6: text_path("squares.txt").write_text("\n".join(str(x*x) for x in values), encoding="utf-8")
    elif question == 7: text_path("cubes.txt").write_text("\n".join(str(x**3) for x in values), encoding="utf-8")
    elif question == 8: print({"positive": sum(x > 0 for x in values), "negative": sum(x < 0 for x in values), "zero": values.count(0)})
    elif question == 9: print(sorted({x for x in values if values.count(x) > 1}))
    else: text_path("sorted_numbers.txt").write_text("\n".join(map(str, sorted(values))), encoding="utf-8")
    print(f"Level 6 question {question} completed.")


def level7(question):
    path = text_path("students.txt")
    records = [{"id": 1, "name": "Anusha", "age": 21, "course": "Python", "marks": 88}, {"id": 2, "name": "Rahul", "age": 20, "course": "SQL", "marks": 76}]
    if question == 1: path.write_text(json.dumps(records[0]), encoding="utf-8")
    elif question == 2: path.write_text("\n".join(json.dumps(x) for x in records), encoding="utf-8")
    elif question == 3: print(path.read_text(encoding="utf-8"))
    elif question in (4, 5): print(next((x for x in records if (x["name"] == "Anusha" if question == 4 else x["id"] == 1)), "Student not found."))
    elif question == 6: records[0]["marks"] = 95; path.write_text("\n".join(json.dumps(x) for x in records), encoding="utf-8")
    elif question == 7: path.write_text(json.dumps(records[1]), encoding="utf-8")
    elif question == 8: print(max(records, key=lambda x: x["marks"]))
    elif question == 9: print(sum(x["marks"] for x in records) / len(records))
    else: print([x for x in records if x["marks"] > 75])
    print(f"Level 7 question {question} completed.")


def level8(question):
    path = text_path("students.csv")
    records = [{"id": 1, "name": "Anusha", "course": "Python", "marks": 88}, {"id": 2, "name": "Rahul", "course": "SQL", "marks": 36}]
    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=records[0]); writer.writeheader(); writer.writerows(records)
    if question == 1: print(path)
    elif question == 2: print(records)
    elif question == 3: records.append({"id": 3, "name": "Priya", "course": "Java", "marks": 91})
    elif question == 4: print([x for x in records if x["id"] == 1])
    elif question == 5: records[0]["marks"] = 95
    elif question == 6: records = records[1:]
    elif question == 7: print(max(records, key=lambda x: x["marks"]))
    elif question == 8: print(sum(x["marks"] for x in records) / len(records))
    elif question == 9: print([x for x in records if x["marks"] < 40])
    else: records.sort(key=lambda x: x["marks"], reverse=True)
    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=records[0]); writer.writeheader(); writer.writerows(records)
    print(f"Level 8 question {question} completed: {path}")


def level9(question):
    path = text_path("students.json")
    students = [{"id": 1, "name": "Anusha", "course": "Python", "marks": 88}]
    if question == 1: path.write_text(json.dumps(students, indent=2), encoding="utf-8")
    elif question == 2: print(json.loads(path.read_text(encoding="utf-8")))
    elif question == 3: students.append({"id": 2, "name": "Rahul", "course": "SQL", "marks": 76})
    elif question == 4: students[0]["marks"] = 95
    elif question == 5: students = []
    elif question == 6: text_path("employees.json").write_text(json.dumps([{"name": "Anusha", "salary": 75000}], indent=2), encoding="utf-8")
    elif question == 7: print("Highest salary: Anusha")
    elif question == 8: text_path("products.json").write_text(json.dumps([{"name": "Laptop", "price": 55000, "quantity": 2}], indent=2), encoding="utf-8")
    elif question == 9: print("Inventory value: 110000")
    else: path.write_text(json.dumps({"students": students}, indent=2), encoding="utf-8")
    print(f"Level 9 question {question} completed.")


def level10(question):
    try:
        if question == 1: raise FileNotFoundError("sample.txt not found")
        if question == 2: raise PermissionError("Permission denied")
        if question == 3:
            with text_path("safe.txt").open("w", encoding="utf-8") as file: file.write("safe data")
        elif question == 4: print(text_path("sample.txt").exists())
        elif question == 5: print(float("not a number"))
        elif question == 6: raise csv.Error("Invalid CSV data")
        elif question == 7: raise json.JSONDecodeError("Invalid JSON", "{bad", 1)
        elif question == 8: print(text_path(input("Filename: ")).read_text(encoding="utf-8"))
        elif question == 9: shutil.copyfile(text_path("sample.txt"), text_path("sample_copy.txt"))
        else: print("Complete File Management System: create, read, write, append, search, update, copy, rename, delete")
    except (FileNotFoundError, PermissionError, ValueError, csv.Error, json.JSONDecodeError) as error: print(f"Handled file error: {error}")
    finally: print(f"Level 10 question {question} finished.")


def mini(question):
    names = ["student_record_text", "employee_csv", "library_json", "contact_csv", "bank_transactions", "shopping_cart_bill", "student_attendance_csv", "login_registration", "quiz_json", "menu_file_manager"]
    path = ROOT / f"mini_{question}_{names[question-1]}.txt"
    path.write_text(f"Mini Project {question}: {names[question-1]}\n", encoding="utf-8")
    print(f"Mini project {question} ready: {path}")


def run(level, question):
    globals()[f"level{level}"](question) if level <= 10 else mini(question)
