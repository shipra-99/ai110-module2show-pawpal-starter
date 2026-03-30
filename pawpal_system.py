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
        """Mark the task as completed."""
        self.completed = True


# ---------------- PET ----------------
@dataclass
class Pet:
    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        """Add a new task to the pet."""
        self.tasks.append(task)

    def get_tasks(self):
        """Return all tasks for the pet."""
        return self.tasks


# ---------------- OWNER ----------------
class Owner:
    def __init__(self, name: str):
        self.name = name
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet):
        """Add a pet to the owner."""
        self.pets.append(pet)

    def get_all_tasks(self):
        """Return all tasks across all pets."""
        all_tasks = []
        for pet in self.pets:
            all_tasks.extend(pet.get_tasks())
        return all_tasks


# ---------------- SCHEDULER ----------------
class Scheduler:
    def __init__(self, owner: Owner):
        self.owner = owner

    def generate_daily_plan(self):
        """Generate a sorted daily plan of tasks."""
        tasks = self.owner.get_all_tasks()
        return self.sort_tasks(tasks)

    def sort_tasks(self, tasks: List[Task]):
        """Sort tasks by priority and time."""
        priority_map = {"high": 1, "medium": 2, "low": 3}

        return sorted(
            tasks,
            key=lambda t: (priority_map.get(t.priority, 4), t.time)
        )

    def detect_conflicts(self, tasks: List[Task]):
        """Detect tasks scheduled at the same time."""
        seen_times = {}
        conflicts = []

        for task in tasks:
            if task.time in seen_times:
                conflicts.append((seen_times[task.time], task))
            else:
                seen_times[task.time] = task

        return conflicts