from dataclasses import dataclass, field
from typing import List
from datetime import datetime, timedelta


# ---------------- TASK ----------------
from datetime import datetime

@dataclass
class Task:
    title: str
    duration: int
    priority: str
    time: str
    completed: bool = False
    frequency: str = None   # "daily", "weekly", or None

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
        tasks = self.owner.get_all_tasks()

        # handle recurrence
        new_tasks = self.handle_recurring_tasks(tasks)

        # combine original + new tasks (temporary, not stored)
        tasks = tasks + new_tasks

        # filter incomplete
        tasks = self.filter_tasks(tasks, completed=False)

        # sort
        tasks = self.sort_by_time(tasks)

        return tasks

    def sort_by_time(self, tasks: List[Task]):
        """Sort tasks by time in HH:MM format."""
        return sorted(tasks, key=lambda t: t.time)

    def filter_tasks(self, tasks: List[Task], completed: bool = None, pet_name: str = None):
        """Filter tasks by completion status or pet name."""
        if completed is not None:
            tasks = [t for t in tasks if t.completed == completed]

        if pet_name is not None:
            tasks = [t for t in tasks if pet_name.lower() in t.title.lower()]

        return tasks

    def detect_conflicts(self, tasks: List[Task]):
         """Detect tasks scheduled at the same time and return warnings."""
        seen_times = {}
        warnings = []

        for task in tasks:
            if task.time in seen_times:
                existing_task = seen_times[task.time]

                warning = (
                    f"Conflict: '{existing_task.title}' and '{task.title}' "
                    f"are both scheduled at {task.time}"
                )
                warnings.append(warning)
            else:
                seen_times[task.time] = task

        return warnings
    
    def handle_recurring_tasks(self, tasks: List[Task]):
           """Generate next occurrence for completed recurring tasks."""
        new_tasks = []

        from datetime import datetime, timedelta
        today = datetime.now()

        for task in tasks:
            if task.completed and task.frequency:

                if task.frequency == "daily":
                    next_date = today + timedelta(days=1)
                elif task.frequency == "weekly":
                    next_date = today + timedelta(days=7)
                else:
                    continue

                new_task = Task(
                    title=task.title,
                    duration=task.duration,
                    priority=task.priority,
                    time=task.time,
                    completed=False,
                    frequency=task.frequency
                )

                new_tasks.append(new_task)

        return new_tasks