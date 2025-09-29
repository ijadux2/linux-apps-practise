
# linux-apps-practise

Small collection of tiny command-line examples implemented in Python. The repository contains two small apps used as practice for building simple Linux CLI tools and unit tests.

Contents
- `greet-py/` — minimal example CLI that greets a name.
- `to-do-list/` — simple to-do list CLI with an importable module and unit tests.

Requirements
- Python 3.8+ (3.10+ recommended)
- For running tests: `pytest` (see `to-do-list/requirements.txt`)

Projects

1) Greet (in `greet-py/`)

Purpose
 - Minimal example showing how to build a CLI with `argparse`.

Usage
 - Run the script directly with Python:

```bash
python3 greet-py/greet.py YourName
python3 greet-py/greet.py YourName --shout
```

Examples
 - `python3 greet-py/greet.py Alice` prints "Hello, Alice!"
 - `python3 greet-py/greet.py Bob --shout` prints "HELLO, BOB!"

2) To-do list (in `to-do-list/`)

Purpose
 - Small to-do manager demonstrating file-backed persistence, dataclasses, and a tiny CLI with subcommands.

Location
 - Script: `to-do-list/to-do.py`
 - Importable module used by tests: `to-do-list/to_do.py` which re-exports the implementation in `to-do-list/to_do_cli.py`.

Data
 - By default tasks are stored in `~/.todo.json`. Use the `--file` / `-f` option to override the path for testing or alternate storage.

CLI usage
 - From the repository root you can run:

```bash
python3 to-do-list/to-do.py add "Buy milk"
python3 to-do-list/to-do.py list
python3 to-do-list/to-do.py complete 2
python3 to-do-list/to-do.py delete 3
python3 to-do-list/to-do.py stats
python3 to-do-list/to-do.py clear
```

Examples (use a custom file to avoid touching your home):

```bash
# add tasks to a temporary file
python3 to-do-list/to-do.py -f /tmp/tasks.json add "Write report"
python3 to-do-list/to-do.py -f /tmp/tasks.json list
python3 to-do-list/to-do.py -f /tmp/tasks.json complete 1
python3 to-do-list/to-do.py -f /tmp/tasks.json stats
```

API (for tests / importing)
 - The module `to-do-list/to_do.py` exposes the functions used by the tests and can be imported directly:
	 - `add_task(path: Path, title: str) -> Task`
	 - `list_tasks(path: Path, show_all: bool = False) -> List[Task]`
	 - `complete_task(path: Path, task_id: int) -> Optional[Task]`
	 - `delete_task(path: Path, task_id: int) -> Optional[Task]`
	 - `clear_tasks(path: Path) -> None`
	 - `load_tasks(path: Path) -> List[Task]`

Running tests

1. Create a virtual environment (optional but recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r to-do-list/requirements.txt
```

2. Run pytest from the `to-do-list` directory:

```bash
cd to-do-list
pytest -q
```

Notes and development
- The to-do implementation stores tasks as a JSON array of dataclass-serializable objects. If the tasks file is missing or corrupted, the code treats it as an empty list.
- The `to-do-list/tests/` directory contains unit tests that exercise the module-level API (they import `to_do`).

Contributing
- Feel free to open issues or submit PRs to add features (tags, due-dates, priority) or improve UX (pretty printing, colors).

License
- This repository does not include a license file. Add one if you plan to share it publicly.

Acknowledgements
- Small practice project for learning CLI patterns and Python testing.
