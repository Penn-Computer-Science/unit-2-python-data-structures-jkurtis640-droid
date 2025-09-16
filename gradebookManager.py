gradebook = {
  "Alice Harry": 70,
  "Michael Terry": 80,
  "Tarkonchenku": 100, # reference to project 1
}
print(gradebook)
gradebook_input_student = input("Enter a student: ")
print(gradebook)
gradebook_input_grade = input("Enter a grade: ")
gradebook[gradebook_input_student] = gradebook_input_grade
print(gradebook)


def average(a,b,c):
    return ((a + b + c) // 3)
     

print("Average: ", str(average(71,54,82)))
a1 = average(80,76,80)
print("Average: ", str(average(80,76,80)))
a2 = average(86,87,100)
print("Average: ", str(average(90,87,100)))
a3 = average(100,100,100)
print("Average: ", str(average(100,100,100)))

if a3 > 92:
   print("Top student: ", average(100,100,100))
elif a3 < 92:
   print("Invalid top student")

print("Top student: ", average(100,100,100))