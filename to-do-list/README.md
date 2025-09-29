# To-Do CLI

A tiny command-line to-do manager written in Python. Tasks are stored in JSON (by default in `~/.todo.json`).

Features:
- Add tasks
- List tasks (hide/show completed)
- Mark tasks complete
- Delete tasks
- Clear all tasks
- Show simple stats

Usage examples:

  python to-do.py add "Buy milk"
  python to-do.py list
  python to-do.py complete 1
  python to-do.py delete 2
  python to-do.py stats

Run tests:

  pip install -r requirements.txt
  pytest
