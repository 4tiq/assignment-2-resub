import unittest
from student_management import Student, StudentManager
from validators import validate_email, validate_student_id, validate_year

class TestStudentFunctions(unittest.TestCase):

    def test_validate_email(self):
        self.assertTrue(validate_email("student@example.com"))
        self.assertFalse(validate_email("bademail"))

    def test_validate_student_id(self):
        self.assertTrue(validate_student_id("ST123"))
        self.assertFalse(validate_student_id("123ST"))

    def test_validate_year(self):
        self.assertTrue(validate_year("3"))
        self.assertFalse(validate_year("5"))

    def test_add_search_student(self):
        sm = StudentManager()
        s = Student("ST001", "Test Student", "test@example.com", "Math", 2)
        self.assertTrue(sm.add_student(s))
        self.assertEqual(sm.search_student("ST001").name, "Test Student")

    def test_update_student(self):
        sm = StudentManager()
        s = Student("ST002", "Sample", "sample@example.com", "Science", 1)
        sm.add_student(s)
        sm.update_student("ST002", "Updated", "upd@example.com", "Physics", 3)
        student = sm.search_student("ST002")
        self.assertEqual(student.name, "Updated")
        self.assertEqual(student.course, "Physics")
        self.assertEqual(student.year, 3)

    def test_delete_student(self):
        sm = StudentManager()
        s = Student("ST003", "Delete Me", "deleteme@example.com", "English", 2)
        sm.add_student(s)
        self.assertTrue(sm.delete_student("ST003"))
        self.assertIsNone(sm.search_student("ST003"))

if __name__ == '__main__':
    unittest.main()
