class Person:
    def __init__(self, last_name, first_name, student_id):
        self.last_name = last_name
        self.first_name = first_name
        self.student_id = student_id

# Test
person1 = Person("NANA", "Prisca", 101)
print("Person information :")
print(f"Last name  : {person1.last_name}")
print(f"First name : {person1.first_name}")
print(f"ID         : {person1.student_id}")
