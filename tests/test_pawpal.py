from pawpal_system import Task, Pet


# ---------------- TEST 1 ----------------
def test_task_completion():
    task = Task("Feed", 10, "high", "08:00")

    # before completion
    assert task.completed is False

    # mark complete
    task.mark_complete()

    # after completion
    assert task.completed is True


# ---------------- TEST 2 ----------------
def test_add_task_to_pet():
    pet = Pet("Max", "dog")

    task = Task("Walk", 30, "high", "09:00")

    # initially empty
    assert len(pet.tasks) == 0

    # add task
    pet.add_task(task)

    # verify count increased
    assert len(pet.tasks) == 1
    assert pet.tasks[0] == task