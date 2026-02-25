Student Registry CLI

A hybrid Python CLI application built to demonstrate modular architecture, object-oriented modeling, and layered design principles. Rather than implementing a single-script solution, this project intentionally separates domain logic, validation, persistence, and interface layers to reflect real-world software structure.

The application allows users to create, update, view, and list student records through either a command-based interface (built with argparse) or an interactive menu mode. Both interfaces rely on the same underlying logic layer, demonstrating a clear separation between user interaction and core application logic.

The system persists data to a JSON file and supports exporting records to CSV. Validation rules are enforced at the service layer to ensure student numbers are numeric, course counts remain within an acceptable range, and names are not blank. By keeping validation outside the CLI layer, the design remains reusable and testable.

The project is structured as a Python package using a layered approach. The models module defines the Student dataclass and its controlled update methods. The service module handles validation and business operations. The storage module isolates JSON serialization and CSV export functionality. Two CLI entry points (cli_commands and cli_menu) provide different user interfaces while sharing the same application logic. Unit tests verify model behavior and validation rules using pytest.

To run the interactive menu:

PYTHONPATH=src python -m student_registry menu

Example of using the command interface:

PYTHONPATH=src python -m student_registry add --name "Karson" --id 1001 --courses 4

PYTHONPATH=src python -m student_registry show --id 1001

PYTHONPATH=src python -m student_registry update-courses --id 1001 --courses 5

To execute the test suite:
pytest

While the original requirement was to implement a simple class-based program, I expanded the scope to focus on maintainable design. Building this project reinforced the importance of separating responsibilities across modules, writing reusable service logic, validating data outside the interface layer, and structuring Python projects as packages rather than standalone scripts. It also provided practical experience working with file-based persistence and automated testing.

Technologies used include Python 3, argparse, dataclasses, JSON and CSV file I/O, and pytest.
