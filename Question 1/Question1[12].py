# Accept marks of 5 subjects
marks = []
for i in range(1, 6):
    mark = int(input(f"Enter marks for subject {i}: "))
    marks.append(mark)

# Display marks
print("\nMarks in 5 subjects:", marks)

# Calculate total and percentage
total = sum(marks)
percentage = total / 5

print(f"Total Marks = {total}")
print(f"Percentage = {percentage:.2f}%")

# Find grade using match-case
match percentage:
    case p if p > 85:
        grade = "A"
    case p if p > 75:
        grade = "B"
    case p if p > 50:
        grade = "C"
    case p if p > 30:
        grade = "D"
    case p if p <= 30:
        grade = "Reappear"
print(f"Grade = {grade}")

# Sample Input/Output
#Enter marks for subject 1: 77
#Enter marks for subject 2: 76
#Enter marks for subject 3: 44
#Enter marks for subject 4: 65
#Enter marks for subject 5: 57
#Marks in 5 subjects: [77, 76, 44, 65, 57]
#Total Marks = 319
#Percentage = 63.80%
#Grade = C