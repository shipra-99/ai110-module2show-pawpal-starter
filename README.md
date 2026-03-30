# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## Smarter Scheduling

The PawPal+ scheduler includes several algorithmic improvements:

- **Sorting:** Tasks are sorted by time to ensure a clear daily schedule.
- **Filtering:** Completed tasks are excluded from the active schedule.
- **Recurring Tasks:** Daily and weekly tasks automatically generate their next occurrence when completed.
- **Conflict Detection:** The system detects tasks scheduled at the same time and provides user-friendly warnings.

These features improve usability while keeping the implementation simple and readable.

## Testing PawPal+

To run the automated test suite:

```bash
python -m pytest
```
What is tested

The test suite verifies the core functionality of the PawPal+ system:

Task Completion: Ensures tasks are correctly marked as completed.
Task Addition: Confirms tasks are properly added to a pet.
Sorting: Verifies that tasks are ordered chronologically by time.
Filtering: Ensures completed tasks are excluded from the active schedule.
Recurring Tasks: Confirms that completing a recurring task generates a new task.
Conflict Detection: Detects and reports tasks scheduled at the same time.


Confidence Level ⭐⭐⭐⭐☆ (4/5)

The system performs reliably across all tested scenarios, including edge cases like empty task lists and scheduling conflicts. While the implementation is intentionally simple (e.g., conflict detection only checks exact time matches), it is stable and meets all project requirements.


## Features

PawPal+ includes several intelligent scheduling features:

- **Task Management:** Add and track pet care tasks such as feeding, walking, and playtime.
- **Sorting by Time:** Tasks are automatically sorted in chronological order to create a clear daily plan.
- **Filtering:** Completed tasks are excluded from the active schedule to keep the plan focused.
- **Recurring Tasks:** Daily and weekly tasks automatically generate their next occurrence when completed.
- **Conflict Detection:** The system detects tasks scheduled at the same time and displays user-friendly warnings.
- **Multi-Pet Support:** Manage tasks across multiple pets through a centralized owner model.