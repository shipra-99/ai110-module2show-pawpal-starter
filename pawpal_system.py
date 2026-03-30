from dataclasses import dataclass, field
from typing import List


# ---------------- TASK ----------------
@dataclass
class Task:
    title: str
    duration: int
    priority: str
    time: str
    completed: bool = False

    def mark_complete(self):
        pass


# ---------------- PET ----------------
@dataclass
class Pet:
    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        pass

    def get_tasks(self):
        pass


# ---------------- OWNER ----------------
class Owner:
    def __init__(self, name: str):
        self.name = name
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet):
        pass

    def get_all_tasks(self):
        pass


# ---------------- SCHEDULER ----------------
class Scheduler:
    def __init__(self, owner: Owner):
        self.owner = owner

    def generate_daily_plan(self):
        pass

    def sort_tasks(self, tasks: List[Task]):
        pass

    def detect_conflicts(self, tasks: List[Task]):
        pass