def get_weather(temp):
    if temp > 20:
        return "hot"
    else: 
        return "cold"

def add(a,b):
    return a + b

def divide(a,b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

class StudentDataManager:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name):
        if student_id in self.students:
            raise ValueError("Student ID already exists")
        self.students[student_id] = name
        return True
    
    def get_student(self, student_id):
        return self.students.get(student_id, None)