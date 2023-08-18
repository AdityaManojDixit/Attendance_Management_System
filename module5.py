class AttendanceSystem:
    # (Existing methods and attributes...)

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

attendance_system = AttendanceSystem()
