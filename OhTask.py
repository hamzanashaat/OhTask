Student1_Name = "Max"
Student1_Math = "C"
Student1_English = "B"
Student1_Science = "A"
Student1 = (Student1_Name, Student1_Math, Student1_English, Student1_Science)
Student2_Name = "Emma"
Student2_Math = "A+"
Student2_English = "B+"
Student2_Science = "A-"
Student2 = (Student2_Name, Student2_Math, Student2_English, Student2_Science)
Student3_Name = "Liam"
Student3_Math = "A-"
Student3_English = "C+"
Student3_Science = "B+"
Student3 = (Student3_Name, Student3_Math, Student3_English, Student3_Science)
Dictionary = (Student1, Student2, Student3)
grade_points = {"A+": 4.3, "A": 4.0, "A-": 3.7,"B+": 3.3, "B": 3.0, "C+": 2.3, "C": 2.0
}
students = [
    ("Max", "C", "B", "A"),
    ("Emma", "A+", "B+", "A-"),
    ("Liam", "A-", "C+", "B+")
]
for name, math, english, science in students:
    grades = [math, english, science]
    average = round(sum(grade_points[g] for g in grades) / 3, 2)
    print(f"{name}'s average is: {average}")
print(Dictionary)