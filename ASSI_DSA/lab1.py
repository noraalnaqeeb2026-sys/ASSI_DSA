# HW1 - Lists & Dictionary

# قائمة الطلاب
students = ["Lana", "Mona", "Sara", "Ola", "Nora"]
students.append("NORA")   # إضافة اسمي

students.remove("Ola")      # حذف طالب

print("Number of students:", len(students))
print("Students List:", students)

# قاموس معلومات الطالب
student_info = {
    "name": "NORA",
    "id": "20251234",
    "major": "IT",
    "level": "Level 2"
}

student_info["GPA"] = 3.8   # إضافة معدل

print("\nStudent Information:")
for key, value in student_info.items():
    print(f"{key} : {value}")
