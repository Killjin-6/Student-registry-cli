from pathlib import Path
from .storage import load_students, save_students, export_csv, DEFAULT_DB_PATH
from .service import validate_student_number, validate_num_courses, add_student, update_courses, get_student, list_students

def prompt(msg: str) -> str:
    return input(msg).strip()

def run(db_path: Path = DEFAULT_DB_PATH) -> int:
    students = load_students(db_path)

    while True:
        print("***** Student Registry Menu *****")
        print("1) Add student")
        print("2) Show student")
        print("3) Update number of courses")
        print("4) List students")
        print("5) Save")
        print("6) Export CSV")
        print("0) Exit")

        choice = prompt("Choose an option: ")

        try:
            if choice == "1":
                name = prompt("Enter name: ")
                sid = validate_student_number(prompt("Enter student number (numeric): "))
                courses = validate_num_courses(prompt("Enter number of courses (0-8): "))
                s = add_student(students, name, sid, courses)
                print("\nCreated student:\n" + s.display())

                # assignment requirement: modify one attribute after creation
                # We’ll do it right here with a prompt (great for your demo video).
                if prompt("Change number of courses now? (y/n): ").lower() == "y":
                    new_courses = validate_num_courses(prompt("Enter NEW number of courses (0-8): "))
                    s2 = update_courses(students, sid, new_courses)
                    print("\nUpdated student:\n" + s2.display())

            elif choice == "2":
                sid = validate_student_number(prompt("Enter student number: "))
                s = get_student(students, sid)
                print("\n" + s.display())

            elif choice == "3":
                sid = validate_student_number(prompt("Enter student number: "))
                new_courses = validate_num_courses(prompt("Enter NEW number of courses (0-8): "))
                s = update_courses(students, sid, new_courses)
                print("\nUpdated student:\n" + s.display())

            elif choice == "4":
                all_s = list_students(students)
                if not all_s:
                    print("No students yet.")
                else:
                    print()
                    for s in all_s:
                        print("-" * 24)
                        print(s.display())

            elif choice == "5":
                save_students(students, db_path)
                print(f"Saved {len(students)} students to {db_path}")

            elif choice == "6":
                csv_name = prompt("Enter CSV filename (example: students.csv): ")
                export_csv(students, Path(csv_name))
                print(f"Exported to {csv_name}")

            elif choice == "0":
                # friendly auto-save
                save_students(students, db_path)
                print(f"Saved. Bye!")
                return 0

            else:
                print("Invalid option.")

        except (ValueError, KeyError) as e:
            print(f"Error: {e}")