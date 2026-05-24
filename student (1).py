
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
        # Part 3 - Magic Method __str__
    def __str__(self):
        return (f"Student: {self.first_name} {self.last_name} | "
                f"ID: {self.student_id} | "
                f"Department: {self.field_of_study} | "
                f"Entry: {self.entry_time}h | "
                f"Late: {'Yes' if self.is_late else 'No'}")

    # Part 4 - Decorator @staticmethod
    @staticmethod
    def check_late(entry_time, class_start=8.0):
        minutes_late = (entry_time - class_start) * 60
        if minutes_late <= 0:
            return "On time"
        return f"Late by {minutes_late:.0f} minutes"

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