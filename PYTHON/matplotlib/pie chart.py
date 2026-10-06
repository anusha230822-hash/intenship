import matplotlib.pyplot as plt
courses = ["Python", "Java", "Data Science", "Web"] 
students = [40, 25, 20, 15]
plt.pie(    students,    labels=courses,    autopct="%1.1f%%" ) 
plt.title("Student Course Distribution")
plt.show()
