#!/usr/bin/env python3
"""Simple To-Do list CLI.

Usage examples:
  python to-do.py add "Buy milk"
  python to-do.py list
  python to-do.py complete 2
  python to-do.py delete 3

Tasks are stored by default in ~/.todo.json. Use --file to override.
"""
from __future__ import annotations
import argparse
import json
from dataclasses import dataclass, asdict
from datetime import datetime
from pathlib import Path
from typing import List, Optional

DEFAULT_FILE = Path.home() / ".todo.json"

@dataclass
class Task:
    id: int
    title: str
    done: bool = False
    created_at: str = ""

    def to_dict(self):
        return asdict(self)


def load_tasks(path: Path) -> List[Task]:
    if not path.exists():
        return []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return [Task(**t) for t in data]
    except Exception:
        # If the file is corrupt, treat as empty list
        return []


def save_tasks(path: Path, tasks: List[Task]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps([t.to_dict() for t in tasks], ensure_ascii=False, indent=2), encoding="utf-8")


def next_id(tasks: List[Task]) -> int:
    if not tasks:
        return 1
    return max(t.id for t in tasks) + 1


def add_task(path: Path, title: str) -> Task:
    tasks = load_tasks(path)
    t = Task(id=next_id(tasks), title=title, done=False, created_at=datetime.utcnow().isoformat())
    tasks.append(t)
    save_tasks(path, tasks)
    return t


def list_tasks(path: Path, show_all: bool = False) -> List[Task]:
    tasks = load_tasks(path)
    if show_all:
        return tasks
    return [t for t in tasks if not t.done]


def complete_task(path: Path, task_id: int) -> Optional[Task]:
    tasks = load_tasks(path)
    for t in tasks:
        if t.id == task_id:
            t.done = True
            save_tasks(path, tasks)
            return t
    return None


def delete_task(path: Path, task_id: int) -> Optional[Task]:
    tasks = load_tasks(path)
    for i, t in enumerate(tasks):
        if t.id == task_id:
            removed = tasks.pop(i)
            save_tasks(path, tasks)
            return removed
    return None


def clear_tasks(path: Path) -> None:
    save_tasks(path, [])


def stats(path: Path) -> dict:
    tasks = load_tasks(path)
    total = len(tasks)
    done = sum(1 for t in tasks if t.done)
    return {"total": total, "done": done, "pending": total - done}


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(prog="to-do", description="Simple to-do list manager")
    parser.add_argument("--file", "-f", help="Path to tasks file", default=str(DEFAULT_FILE))

    sub = parser.add_subparsers(dest="cmd", required=True)

    p_add = sub.add_parser("add", help="Add a new task")
    p_add.add_argument("title", help="Task title")

    p_list = sub.add_parser("list", help="List tasks")
    p_list.add_argument("--all", action="store_true", help="Show completed tasks too")

    p_complete = sub.add_parser("complete", help="Mark a task complete")
    p_complete.add_argument("id", type=int, help="Task id")

    p_delete = sub.add_parser("delete", help="Delete a task")
    p_delete.add_argument("id", type=int, help="Task id")

    p_clear = sub.add_parser("clear", help="Remove all tasks")

    p_stats = sub.add_parser("stats", help="Show task stats")

    args = parser.parse_args(argv)
    path = Path(args.file).expanduser()

    if args.cmd == "add":
        t = add_task(path, args.title)
        print(f"Added: [{t.id}] {t.title}")
        return 0

    if args.cmd == "list":
        tasks = list_tasks(path, show_all=args.all)
        if not tasks:
            print("No tasks.")
            return 0
        for t in tasks:
            status = "x" if t.done else " "
            print(f"[{t.id}] [{status}] {t.title}")
        return 0

    if args.cmd == "complete":
        t = complete_task(path, args.id)
        if t:
            print(f"Completed: [{t.id}] {t.title}")
            return 0
        print("Task not found")
        return 2

    if args.cmd == "delete":
        t = delete_task(path, args.id)
        if t:
            print(f"Deleted: [{t.id}] {t.title}")
            return 0
        print("Task not found")
        return 2

    if args.cmd == "clear":
        clear_tasks(path)
        print("All tasks removed.")
        return 0

    if args.cmd == "stats":
        s = stats(path)
        print(f"Total: {s['total']}, Done: {s['done']}, Pending: {s['pending']}")
        return 0

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
