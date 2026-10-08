marks = [45, 78, 62, 89, 55, 92, 38, 76]

highest = max(marks)
lowest = min(marks)

average = sum(marks) / len(marks)

count_above = 0
for mark in marks:
    if mark > average:
        count_above += 1

sorted_marks = sorted(marks)

print("Highest mark:", highest)
print("Lowest mark:", lowest)
print("Average mark:", lowest)
print("Students above average:", count_above)
print("Marks in ascending order:", sorted_marks)
