class Student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(student_list):
  #Sort the list of students in descending order of CGPA key=lambda student: student.cgpa,
  sorted_students = sorted(student_list,
       key=lambda student:student.cgpa,
       reverse=True)
#Syntax - lambda argexp
  return sorted_students


#Example usage:
students = [
    Student("Uva", "22bcs13", 7.8),
    Student("Saline", "22bcs12", 8.9),
    Student("Babu", "22bcs11", 9.1),
    Student("Alagu", "22bcs10", 9.9),
]

sorted_students = sort_students(students)

# Print the sorted list of students
for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name,
                                          student.roll_number,
                                                             student.cgpa))