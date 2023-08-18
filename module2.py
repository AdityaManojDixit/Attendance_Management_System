class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

class StudentDatabase:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def view_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def update_student(self, student_id, new_name):
        student = self.view_student(student_id)
        if student:
            student.name = new_name
            return True
        return False

    def delete_student(self, student_id):
        student = self.view_student(student_id)
        if student:
            self.students.remove(student)
            return True
        return False

student_db = StudentDatabase()
