import pytest
from Student_Registry.models import Student

def test_create_student_valid():
    s = Student(name="Karson", student_number=1001, num_courses=3)
    assert s.name == "Karson"
    assert s.student_number == 1001
    assert s.num_courses == 3

def test_blank_name_raises_error():
    s = Student(name="Test", student_number=1, num_courses=1)
    with pytest.raises(ValueError):
        s.update_name("")

def test_invalid_course_number_raises_error():
    s = Student(name="Test", student_number=1, num_courses=1)
    with pytest.raises(ValueError):
        s.update_num_courses(10)

def test_update_courses_success():
    s = Student(name="Test", student_number=1, num_courses=2)
    s.update_num_courses(5)
    assert s.num_courses == 5