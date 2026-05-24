
from person import Person

class Student(Person):
    def __init__(self, last_name, first_name, student_id, field_of_study, entry_time, exit_time):
        # Call the parent constructor via super()
        super().__init__(last_name, first_name, student_id)

        # Attributes specific to Student
        self.field_of_study = field_of_study
        self.entry_time = entry_time    # float ex: 8.5 for 8:30
        self.exit_time = exit_time      # float ex: 12.0 for 12:00

        # is_late: True if the student arrived after 8.0 (8h00)
        self.is_late = entry_time > 8.0

# Test
student1 = Student("SOME", "Mounira", 102, "Computer Science", 8.5, 12.0)
print("Student information :")
print(f"Last name    : {student1.last_name}")
print(f"First name   : {student1.first_name}")
print(f"ID           : {student1.student_id}")
print(f"Department   : {student1.field_of_study}")
print(f"Entry time   : {student1.entry_time}h")
print(f"Exit time    : {student1.exit_time}h")
print(f"Is late      : {student1.is_late}")