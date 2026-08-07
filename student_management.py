import os
from validators import validate_email, validate_student_id, validate_year

FILENAME = "students.txt"

class Person:
    """Base class for a person with name and email."""
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def update_details(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f"{self.name} | {self.email}"


class Student(Person):
    """
    Represents a student with an ID, course, and year of study.
    Inherits from Person.
    """

    def __init__(self, student_id, name, email, course, year):
        super().__init__(name, email)
        self.student_id = student_id
        self.course = course
        self.year = int(year)

    def update_details(self, name, email, course, year):
        super().update_details(name, email)
        self.course = course
        self.year = int(year)

    def to_file_string(self):
        return f"{self.student_id},{self.name},{self.email},{self.course},{self.year}"

    def __str__(self):
        return f"{self.student_id} | {super().__str__()} | {self.course} | Year {self.year}"


class StudentManager:
    """Manages a collection of students."""

    def __init__(self):
        self.students = {}

    def add_student(self, student):
        if student.student_id in self.students:
            return False
        self.students[student.student_id] = student
        return True

    def delete_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            return True
        return False

    def search_student(self, student_id):
        return self.students.get(student_id)

    def update_student(self, student_id, name, email, course, year):
        student = self.search_student(student_id)
        if student:
            student.update_details(name, email, course, year)
            return True
        return False

    def view_students(self):
        return list(self.students.values())


def load_students(manager):
    """Loads students from file into the manager."""
    if not os.path.exists(FILENAME):
        return
    try:
        with open(FILENAME, "r") as file:
            for line in file:
                data = line.strip().split(",")
                if len(data) == 5:
                    student_id, name, email, course, year = data
                    student = Student(student_id, name, email, course, int(year))
                    manager.students[student_id] = student
    except IOError:
        print("Error: Could not read the students file.")


def save_students(manager):
    """Saves all students from manager to file."""
    try:
        with open(FILENAME, "w") as file:
            for student in manager.students.values():
                file.write(student.to_file_string() + "\n")
    except IOError:
        print("Error: Could not write to the students file.")


def add_student(manager):
    """Prompts user for student details and adds to manager."""
    student_id = input("Enter Student ID (Format ST001): ")
    if not validate_student_id(student_id):
        print("Invalid Student ID. Format should be: ST001")
        return

    if manager.search_student(student_id):
        print("Student ID already exists.")
        return

    name = input("Enter Name: ")
    email = input("Enter Email: ")
    if not validate_email(email):
        print("Invalid email format.")
        return

    course = input("Enter Course: ")
    year = input("Enter Year (1-4): ")
    if not validate_year(year):
        print("Invalid year. Please enter a number between 1 and 4.")
        return

    student = Student(student_id, name, email, course, year)
    manager.add_student(student)
    print("Student added successfully.")


def view_students(manager):
    """Displays all students."""
    students = manager.view_students()
    if not students:
        print("No students found.")
        return
    for student in students:
        print(student)


def search_student(manager):
    """Searches and displays a student by ID."""
    student_id = input("Enter Student ID: ")
    student = manager.search_student(student_id)
    if student:
        print(student)
    else:
        print("Student not found.")


def update_student(manager):
    """Update details for an existing student."""
    student_id = input("Enter Student ID to update: ")
    student = manager.search_student(student_id)
    if not student:
        print("Student not found.")
        return

    name = input("Enter new name: ")
    email = input("Enter new email: ")
    if not validate_email(email):
        print("Invalid email format.")
        return

    course = input("Enter new course: ")
    year = input("Enter new year (1-4): ")
    if not validate_year(year):
        print("Invalid year.")
        return

    manager.update_student(student_id, name, email, course, year)
    print("Student updated successfully.")


def delete_student(manager):
    """Deletes a student after confirmation."""
    student_id = input("Enter Student ID to delete: ")
    student = manager.search_student(student_id)
    if not student:
        print("Student not found.")
        return

    confirm = input(f"Are you sure you want to delete {student.name} (ID: {student_id})? (y/n): ")
    if confirm.lower() == 'y':
        manager.delete_student(student_id)
        print("Student deleted.")
    else:
        print("Deletion cancelled.")


def main():
    manager = StudentManager()
    load_students(manager)

    while True:
        print("\nStudent Management System")
        print("1. View Students")
        print("2. Add Student")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Save Students")
        print("7. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            view_students(manager)
        elif choice == "2":
            add_student(manager)
        elif choice == "3":
            search_student(manager)
        elif choice == "4":
            update_student(manager)
        elif choice == "5":
            delete_student(manager)
        elif choice == "6":
            save_students(manager)
            print("Students saved.")
        elif choice == "7":
            save_students(manager)
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main()

