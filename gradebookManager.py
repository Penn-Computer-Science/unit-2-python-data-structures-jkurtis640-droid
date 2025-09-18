
## This  takes place 1000 years before the arcturia since tarkonchenku is 1016 years old and he iss in high school
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

new_gradebook = ["Alice Harry","Michael Terry","Tarkonchenku"]
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

print("Top student: ", new_gradebook[2])
yes = "yes"
no = "no"
expel_student = input("Do you want to remove a student: ")
if expel_student == no:
   print("I will keep the grade book the same. ")
if expel_student == yes:
   student_expel = input("Which student do you want to remove ")
   try:
      if student_expel == "Alice Harry":
         remove_student = new_gradebook.remove("Alice Harry")
         print("Removed Alice Harry! ")
      elif student_expel == "Michael Terry":
         remove_student = new_gradebook.remove("Michael Terry")
         print("Removed Michael Terry! ")
      elif student_expel == "Tarkonchenku":
         remove_student = new_gradebook.remove("Tarkonchenku")
         print("Great you removed the top student and you destroyed the space time continuum ")
   except ValueError:
      if student_expel == "Joe Kurtis":
         remove_student = new_gradebook.remove("Joe Kurtis")
         print("Great you destroyed my future ")
         ## Secret creator ending
      else:
         print("Don't remove some one you just added ")
      if gradebook < 90:
         print("Student has an A")
      elif gradebook < 80 and gradebook < 90:
         print("Student has a B") 
      elif gradebook < 70 and gradebook < 80:
         print("Student has a C")
      elif gradebook < 60 and gradebook < 70:
         print("Student has a D")
      elif gradebook < 60:
         print("Student has an F")
      new_gradebook.sort()


