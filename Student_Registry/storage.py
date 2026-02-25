import json
import csv
from pathlib import Path
from typing import List, Dict
from .models import Student

DEFAULT_DB_PATH = Path("students.json")

def load_students(path: Path = DEFAULT_DB_PATH) -> Dict[int, Student]:
    if not path.exists():
        return{}

    data = json.loads(path.read_text(encoding="utf-8"))
    students: Dict[int, Student] = {}
    for item in data:
        s = Student.from_dict(item)
        students[s.student_number] = s
    return students

def save_students(students: Dict[int, Student], path: Path = DEFAULT_DB_PATH) -> None:
    data = [s.to_dict() for s in students.values()]
    path.write_text(json.dumps(data, indent = 2), encoding="utf-8")

def export_csv(students: Dict[int, Student], path: Path = DEFAULT_DB_PATH) -> None:
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "student number", "number of courses"])
        writer.writeheader()
        for s in students.values():
            writer.writerow(s.to_dict())
