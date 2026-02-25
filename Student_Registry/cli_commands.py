import argparse
from pathlib import Path

from .storage import load_students, save_students, export_csv, DEFAULT_DB_PATH
from .service import add_student, update_courses, get_student, list_students

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="student_registry", description="Student Registry CLI (Hybrid)")
    p.add_argument("--db", type=Path, default=DEFAULT_DB_PATH, help="Path to students JSON database")
    sub = p.add_subparsers(dest="cmd", required=True)

    addp = sub.add_parser("add", help="Add a new student")
    addp.add_argument("--name", required=True)
    addp.add_argument("--id", required=True, type=int, dest="student_number")
    addp.add_argument("--courses", required=True, type=int, dest="num_courses")

    showp = sub.add_parser("show", help="Show a student")
    showp.add_argument("--id", required=True, type=int, dest="student_number")

    upp = sub.add_parser("update-courses", help="Update number of courses for a student")
    upp.add_argument("--id", required=True, type=int, dest="student_number")
    upp.add_argument("--courses", required=True, type=int, dest="num_courses")

    lp = sub.add_parser("list", help="List all students")

    ex = sub.add_parser("export", help="Export all students to CSV")
    ex.add_argument("--csv", required=True, type=Path, dest="csv_path")

    return p

def run(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    students = load_students(args.db)

    try:
        if args.cmd == "add":
            s = add_student(students, args.name, args.student_number, args.num_courses)
            save_students(students, args.db)
            print("Added:\n" + s.display())

        elif args.cmd == "show":
            s = get_student(students, args.student_number)
            print(s.display())

        elif args.cmd == "update-courses":
            s = update_courses(students, args.student_number, args.num_courses)
            save_students(students, args.db)
            print("Updated:\n" + s.display())

        elif args.cmd == "list":
            all_s = list_students(students)
            if not all_s:
                print("No students yet.")
            else:
                for s in all_s:
                    print("-" * 24)
                    print(s.display())

        elif args.cmd == "export":
            export_csv(students, args.csv_path)
            print(f"Exported {len(students)} students to {args.csv_path}")

        return 0

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
        return 1