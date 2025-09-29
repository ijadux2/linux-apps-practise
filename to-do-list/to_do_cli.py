#!/usr/bin/env python3
"""Module implementation for import in tests. Mirrors the top-level script."""
from __future__ import annotations
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
