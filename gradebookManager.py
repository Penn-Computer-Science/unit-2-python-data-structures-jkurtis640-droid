gradebook = {
  "Alice Harry": 70,
  "Michael Terry": 80,
  "Tarkonchenku": 100, # reference to project 1
}
print(gradebook)
gradebook_input_student = input("Enter a student: ")
gradebook_input_grade = input("Enter a grade:")
gradebook[gradebook_input_student] =  gradebook_input_grade
print(gradebook)

def average(a,b,c):
    average_grade = a + b + c // 3
    return average_grade


average(71,54,82)
print("Average: ", average)
average(80,76,80)
print("Average: ", average)
average(90,87,100)
print("Average: ", average)
average(100,100,100)
print("Average: ", average)

