from __future__ import annotations
from dataclasses import dataclass,asdict

@dataclass
class Student:
    name: str
    student_number: int
    num_courses: int

    def update_name (self, new_name: str) -> None:
        new_name = new_name.strip()
        if not new_name:
            raise ValueError("Name cannot be empty")
        self.name = new_name

    def update_num_courses(self, new_num_courses: int) -> None:
        if not(0 <= new_num_courses <= 8):
            raise ValueError("Number of courses must be between 0 and 8")
        self.num_courses = new_num_courses

    def display(self) -> str:
        #displays each attribute
        return (
            f"Name: {self.name}\n" 
            f"Student Number: {self.student_number}\n" 
            f"Number of Courses: {self.num_courses}\n"
        )

    def to_dict(self) -> dict:
        return asdict(self)

    @staticmethod
    def from_dict(data: dict) -> Student:
        return Student(
            name = str(data["Name:"]),
            student_number = int(data["Student number:"]),
            num_courses = int(data["Number of courses: "]),
        )