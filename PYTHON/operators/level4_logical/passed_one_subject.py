maths_marks = 35
science_marks = 65
passed_maths = maths_marks >= 40
passed_science = science_marks >= 40
passed_one = passed_maths or passed_science
print("Passed at least one subject:", passed_one)