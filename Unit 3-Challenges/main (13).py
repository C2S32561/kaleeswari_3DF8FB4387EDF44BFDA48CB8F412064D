class Student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(student_list):
  #Sort the list of students in descending order of CGPA key=lambda student: student.cgpa,
  sorted_students = sorted(student_list,
       key=lambda student: student.cgpa,
       reverse=True)
#Syntax - lambda arg:exp
  return sorted_students


#Example usage:
students = [
    Student("Suriya", "A123", 9.9),
    Student("Arasu", "A124", 8.9),
    Student("Deepak","A127",8.1),
    Student("Arjun", "A125", 9.1),
    Student("Ram", "A126", 7.8),
]
  
sorted_students = sort_students(students)

# Print the sorted list of students
for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name,
                                    student.roll_number,
                                                     student.cgpa))