import csv

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class AuthenticationSystem:
    def __init__(self):
        self.users = []

    def register_user(self, username, password):
        self.users.append(User(username, password))

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                return True
        return False

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

class AttendanceSystem:
    def __init__(self):
        self.attendance_records = {}

    def mark_attendance(self, date, student_id):
        if date not in self.attendance_records:
            self.attendance_records[date] = []
        
        if student_id not in self.attendance_records[date]:
            self.attendance_records[date].append(student_id)
            return True  # Attendance marked successfully
        else:
            return False  # Attendance already marked for this student on this date

    def get_students_for_attendance(self):
        return student_db.students

    def view_individual_attendance(self, student_id):
        individual_attendance = {}
        for date, students in self.attendance_records.items():
            if student_id in students:
                individual_attendance[date] = "Present"
            else:
                individual_attendance[date] = "Absent"
        return individual_attendance

    def filter_records_by_date(self, start_date, end_date):
        filtered_records = {}
        for date, students in self.attendance_records.items():
            if start_date <= date <= end_date:
                filtered_records[date] = students
        return filtered_records

    def generate_report(self, date_range):
        report = {}
        for date, students in self.attendance_records.items():
            if date_range[0] <= date <= date_range[1]:
                report[date] = students
        return report

    def generate_summary(self, report):
        summary = {}
        for date, students in report.items():
            summary[date] = {
                "Present": len(students),
                "Absent": len(student_db.students) - len(students)
            }
        return summary

    def export_to_csv(self, data, filename):
        with open(filename, "w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["Date", "Present", "Absent"])
            for date, stats in data.items():
                writer.writerow([date, stats["Present"], stats["Absent"]])

auth_system = AuthenticationSystem()
student_db = StudentDatabase()
attendance_system = AttendanceSystem()

while True:
    print("1. Login")
    print("2. Register")
    print("3. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        print("Login")
        username = input("Username: ")
        password = input("Password: ")
        
        if auth_system.login(username, password):
            print("Login successful.")
            break
        else:
            print("Incorrect username or password. Please try again.")
            
    elif choice == "2":
        print("Register")
        username = input("Username: ")
        password = input("Password: ")
        auth_system.register_user(username, password)
        print("Registration successful. You can now log in.")
        
    elif choice == "3":
        print("Exiting...")
        break
        
    else:
        print("Invalid choice. Please select a valid option.")

if auth_system.login(username, password):
    while True:
        print("1. Add Student")
        print("2. View Student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Mark Attendance")
        print("6. View Individual Attendance")
        print("7. Filter Records by Date")
        print("8. Generate Report")
        print("9. Generate Summary")
        print("10. Export to CSV")
        print("11. Logout")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            student_id = int(input("Enter student ID: "))
            name = input("Enter student name: ")
            student_db.add_student(Student(student_id, name))
            print("Student added successfully.")
            
        elif choice == "2":
            student_id = int(input("Enter student ID: "))
            student = student_db.view_student(student_id)
            if student:
                print(f"Student ID: {student.student_id}, Name: {student.name}")
            else:
                print("Student not found.")
                
        elif choice == "3":
            student_id = int(input("Enter student ID: "))
            new_name = input("Enter new name: ")
            if student_db.update_student(student_id, new_name):
                print("Student updated successfully.")
            else:
                print("Student not found.")
                
        elif choice == "4":
            student_id = int(input("Enter student ID: "))
            if student_db.delete_student(student_id):
                print("Student deleted successfully.")
            else:
                print("Student not found.")
                
        elif choice == "5":
            date = input("Enter date (YYYY-MM-DD): ")
            students = attendance_system.get_students_for_attendance()
            
            print("Available Students:")
            for student in students:
                print(f"ID: {student.student_id}, Name: {student.name}")
                
            student_id = int(input("Enter student ID to mark attendance: "))
            
            if attendance_system.mark_attendance(date, student_id):
                print("Attendance marked successfully.")
            else:
                print("Attendance already marked for this student on this date.")
                
        elif choice == "6":
            student_id = int(input("Enter student ID: "))
            individual_attendance = attendance_system.view_individual_attendance(student_id)
            
            print("Individual Attendance:")
            for date, status in individual_attendance.items():
                print(f"Date: {date}, Status: {status}")
                
        elif choice == "7":
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            date_range = (start_date, end_date)
            filtered_records = attendance_system.filter_records_by_date(start_date, end_date)
            
            print("Filtered Attendance Records:")
            for date, students in filtered_records.items():
                print(f"Date: {date}, Students: {students}")
                
        elif choice == "8":
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            date_range = (start_date, end_date)
            report = attendance_system.generate_report(date_range)
            
            print("Attendance Report:")
            for date, students in report.items():
                print(f"Date: {date}, Students: {students}")
                
        elif choice == "9":
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            date_range = (start_date, end_date)
            report = attendance_system.generate_report(date_range)
            summary = attendance_system.generate_summary(report)
            
            print("Attendance Summary:")
            for date, stats in summary.items():
                print(f"Date: {date}, Present: {stats['Present']}, Absent: {stats['Absent']}")
                
        elif choice == "10":
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            date_range = (start_date, end_date)
            report = attendance_system.generate_report(date_range)
            summary = attendance_system.generate_summary(report)
            
            filename = input("Enter CSV filename: ")
            attendance_system.export_to_csv(summary, filename)
            print("CSV export successful.")
            
        elif choice == "11":
            print("Logging out...")
            break
            
        else:
            print("Invalid choice. Please select a valid option.")
