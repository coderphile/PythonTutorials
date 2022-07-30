student_scores = input("Input a list of Student Scores followed by a space.\n").split(" ")
highest_marks = 0
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
    if student_scores[n] > highest_marks:
        highest_marks = student_scores[n]
print(f"Highest Score in the class is: {highest_marks}")
