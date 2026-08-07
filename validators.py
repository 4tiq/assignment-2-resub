import re

def validate_email(email):
    """
    Validates email format using regex.
    Returns True if valid, False otherwise.
    """
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def validate_student_id(student_id):
    """
    Checks if student ID matches format STxxx where x is digit.
    """
    pattern = r'^ST[0-9]{3}$'
    return re.match(pattern, student_id) is not None

def validate_year(year):
    """
    Validates that the year is a digit between 1 and 4 inclusive.
    """
    return year.isdigit() and 1 <= int(year) <= 4
