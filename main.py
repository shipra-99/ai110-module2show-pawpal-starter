from pawpal_system import Owner, Pet, Task, Scheduler


def main():
    # Create owner
    owner = Owner("Ashutosh")

    # Create pets
    dog = Pet("Max", "dog")
    cat = Pet("Kitty", "cat")

    # 🔹 Add tasks (OUT OF ORDER now)
    dog.add_task(Task("Morning Walk", 30, "high", "09:00"))
    cat.add_task(Task("Play", 20, "medium", "07:30"))  # changed time
    dog.add_task(Task("Feed", 10, "high", "08:00", frequency="daily"))
    dog.add_task(Task("Vet Visit", 30, "high", "09:00"))  # same time as walk

    # Add pets to owner
    owner.add_pet(dog)
    owner.add_pet(cat)

    # Create scheduler
    scheduler = Scheduler(owner)

    # Generate plan (this now uses sorting + filtering)
    plan = scheduler.generate_daily_plan()

    # 🔹 Print sorted schedule
    print("\nSorted Schedule:\n" + "-" * 30)
    for task in plan:
        print(f"{task.time} | {task.title} | Priority: {task.priority.capitalize()}")

    # 🔹 Test filtering (incomplete tasks)
    print("\nFiltered (incomplete only):")
    filtered = scheduler.filter_tasks(owner.get_all_tasks(), completed=False)
    for task in filtered:
        print(task.title)

    # Check conflicts
    conflicts = scheduler.detect_conflicts(plan)

    if conflicts:
        print("\n⚠️ Conflicts detected:")
        for warning in conflicts:
            print(f"- {warning}")
    else:
        print("\nNo conflicts detected.")


if __name__ == "__main__":
    main()