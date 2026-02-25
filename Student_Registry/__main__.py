import sys
from .cli_commands import run as run_commands
from .cli_menu import run as run_menu

def main() -> int:
    #if first arg is "menu", run menu mode.
    if len(sys.argv) >= 2 and sys.argv[1] == "menu":
        return run_menu()
    return run_commands(sys.argv[1:])

if __name__ == "__main__":
    raise SystemExit(main())