class AttendanceSystem:
    # (Existing methods and attributes...)

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

attendance_system = AttendanceSystem()
