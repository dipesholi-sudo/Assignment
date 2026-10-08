student = {
    "name": "Dipesh",
    "age": 21,
    "course": "BscSE",
    "marks": 99
}

# Display the student's information
print("Student information:")
for key, value in student.items():
    print(key + ":", value)

# Increase the marks by 5
student["marks"] += 5

# Add the status key
if student["marks"] >=40:
    student["status"] = "Pass"
else:
    student["status"] = "Fail"

# Display the updated dictionary
print("Updated dictionary:")
print(student)