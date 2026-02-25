from typing import Dict, List
from .models import Student

def validate_student_number(value: str) -> int:
    value = value.strip()
    if not value.isdigit():
        raise ValueError("Student number must be numeric.")
    return int(value)

def validate_num_courses(value: str) -> int:
    value = value.strip()
    if not value.isdigit():
        raise ValueError("Number of courses cannot be negative.")
    n = int(value)
    if not 0 <= n <= 8:
        raise ValueError("Number of courses must be between 0 and 8.")
    return n

def add_student(students: Dict[int, Student], name: str, student_number: int, num_courses: int) -> None:
    if student_number in students:
        raise ValueError(f"Student #{student_number} already exists.")
    s = Student(name=name.strip(), student_number=student_number, num_courses=num_courses)
    # triggers validation via methods for consistency
    s.update_name(s.name)
    s.update_num_courses(num_courses)
    students[student_number] = s
    return s

def get_student(students: Dict[int, Student], student_number: int) -> Student:
    if student_number not in students:
        raise KeyError(f"Student #{student_number} not found.")
    return students[student_number]

def update_courses(students: Dict[int, Student], student_number: int, new_num_courses: int) -> Student:
    s = get_student(students, student_number)
    s.update_num_courses(new_num_courses)
    return s

def list_students(students: Dict[int, Student]) -> List[Student]:
    return sorted(students.values(), key=lambda s: s.student_number)