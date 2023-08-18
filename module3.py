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

attendance_system = AttendanceSystem()
