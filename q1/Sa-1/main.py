class AssignmentSubmission:
    def __init__(self, 
                 student_name: str,
                 student_id: str, 
                 assignment_title: str, 
                 due_date: str, 
                 is_submitted= False, 
                 grade=0.0):
        self.student_name = student_name
        self.student_id = student_id
        self._assignment_title = assignment_title
        self._due_date = due_date
        self.__is_submitted = bool
        self.__grade = grade
        self.__submitted_files = []

    def __validate_grade(self, score):
        if 0.0 <= score <= 100.0:
            return True
        else:
            raise ValueError("Score must be between 0.0 and 100.0")

    def __check_submission_status(self):
        if self.__submitted_files != []:
            return True
        else:
            return False

    def __is_duplicate(self, filename):
        return filename in self.__submitted_files

    def add_file(self, filename):
        if self.__is_duplicate(filename):
            print(f"File '{filename}' is already attached!.")
        else:
            self.__submitted_files.append(filename)
            print(f"{self.student_name} attached '{filename}.' Total files: {len(self.__submitted_files)}.")

    def remove_file(self, filename):
        if filename in self.__submitted_files:
            self.__submitted_files.remove(filename)
            print(f"{self.student_name} removed '{filename}.' Total files: {len(self.__submitted_files)}.")
        elif self.__check_submission_status() and self.__grade > 0.0:
            print(f"{self.student_name} cannot remove files. Assignment already graded.")
        else:
            print(f"File '{filename}' not found in the submission list.")

    def assign_grade(self, score):
        if not self.__check_submission_status():
            print(f"No files submitted for {self.student_name}")
        else:
            if self.__validate_grade(score):
                self.__grade = score
                print(f"Grade {self.__grade} officially assigned to {self.student_name}")

    def get_grade(self):
        return self.__grade

    def view_files(self):
        if self.__submitted_files:
            return str(self.__submitted_files)
        else:
            print("No files submitted yet.")

    def get_status_report(self):
        print(f"ID: {self.student_id} | Name: {self.student_name} | Status: {'Submitted' if self.__check_submission_status() else 'Missing'} | Grade: {'Not Graded' if self.__grade == 0.0 else self.__grade} ")

print("--- INITIALIZING DROPBOX FOR STUDENTS --- ")
student1 = AssignmentSubmission("Alex Gonzaga", "pshs-1090-x", "CS101", "2026-10-01")
student2 = AssignmentSubmission("Adelle", "pshs-1920-x", "CS103", "2026-10-01")
student3 = AssignmentSubmission("Juan dela Cruz", "pshs-1033-x", "CS101", "2026-10-01")
student4 = AssignmentSubmission("Maria Santos", "pshs-1044-x", "CS101", "2026-10-01")
student5 = AssignmentSubmission("Jose Reyes", "pshs-1055-x", "CS101", "2026-10-01")
print()

print(" --- TEST SCENARIO 1: Multiple Files via List ---")
student1.add_file("main.py")
student1.add_file("report.pdf")
student1.assign_grade(95)
print(f"Alex's Files: {student1.view_files()}\n")

print(" --- TEST SCENARIO 2: Removing Files via List ---")
student2.add_file("wrong_homework.docx")
student2.remove_file("wrong_homework.docx")
student2.add_file("correct_project.py")
student2.assign_grade(88)
print(f"Adelle's Files: {student2.view_files()}\n")

print(" --- TEST SCENARIO 3: Preventing Duplicate Files ---")
student3.add_file("script.py")
student3.add_file("script.py")  
print(f"Juan's Files: {student3.view_files()}\n")

print("--- TEST SCENARIO 4: Removing file after being graded ---")
student4.add_file("exam_answer.pdf")
student4.assign_grade(75)
student4.remove_file("exam_answer.pdf") 
print()

print("--- TEST SCENARIO 5: Empty List Handling ---")
student5.add_file("draft.txt")
student5.remove_file("draft.txt")
student5.assign_grade(100)
print()


print("--- FINAL SYSTEM REPORT ---")
print(student1.get_status_report())
print(student2.get_status_report())
print(student3.get_status_report())
print(student4.get_status_report())
print(student5.get_status_report())
