from pawpal_system import Owner, Pet, Task, Scheduler


# ---------------- EXISTING TESTS ----------------
def test_task_completion():
    task = Task("Feed", 10, "high", "08:00")
    assert task.completed is False

    task.mark_complete()
    assert task.completed is True


def test_add_task_to_pet():
    pet = Pet("Max", "dog")
    task = Task("Walk", 30, "high", "09:00")

    assert len(pet.tasks) == 0

    pet.add_task(task)

    assert len(pet.tasks) == 1
    assert pet.tasks[0] == task


# ---------------- NEW TESTS ----------------

# ✅ 1. Sorting Correctness
def test_sorting_by_time():
    owner = Owner("Test")
    pet = Pet("Max", "dog")

    pet.add_task(Task("Walk", 30, "high", "09:00"))
    pet.add_task(Task("Feed", 10, "high", "08:00"))
    pet.add_task(Task("Play", 20, "medium", "07:30"))

    owner.add_pet(pet)

    scheduler = Scheduler(owner)
    plan = scheduler.generate_daily_plan()

    times = [task.time for task in plan]

    assert times == ["07:30", "08:00", "09:00"]


# ✅ 2. Recurrence Logic
def test_recurring_task_creates_new_task():
    owner = Owner("Test")
    pet = Pet("Max", "dog")

    task = Task("Feed", 10, "high", "08:00", frequency="daily")
    pet.add_task(task)
    owner.add_pet(pet)

    # mark complete
    task.mark_complete()

    scheduler = Scheduler(owner)
    plan = scheduler.generate_daily_plan()

    titles = [t.title for t in plan]

    # new "Feed" task should exist
    assert "Feed" in titles


# ✅ 3. Conflict Detection
def test_conflict_detection():
    owner = Owner("Test")
    pet = Pet("Max", "dog")

    pet.add_task(Task("Walk", 30, "high", "09:00"))
    pet.add_task(Task("Vet", 30, "high", "09:00"))

    owner.add_pet(pet)

    scheduler = Scheduler(owner)
    plan = scheduler.generate_daily_plan()

    conflicts = scheduler.detect_conflicts(plan)

    assert len(conflicts) == 1
    assert "Conflict" in conflicts[0]


# ✅ 4. Edge Case: No tasks
def test_no_tasks():
    owner = Owner("Test")
    scheduler = Scheduler(owner)

    plan = scheduler.generate_daily_plan()

    assert plan == []