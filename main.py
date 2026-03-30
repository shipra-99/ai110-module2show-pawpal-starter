from pawpal_system import Owner, Pet, Task, Scheduler


def main():
    # Create owner
    owner = Owner("Ashutosh")

    # Create pets
    dog = Pet("Max", "dog")
    cat = Pet("Kitty", "cat")

    # Add tasks (different times + priorities)
    dog.add_task(Task("Morning Walk", 30, "high", "09:00"))
    dog.add_task(Task("Feed", 10, "high", "08:00"))
    cat.add_task(Task("Play", 20, "medium", "09:30"))

    # Add pets to owner
    owner.add_pet(dog)
    owner.add_pet(cat)

    # Create scheduler
    scheduler = Scheduler(owner)

    # Generate plan
    plan = scheduler.generate_daily_plan()

    # Print schedule nicely
    print("\nToday's Schedule:\n" + "-" * 30)

    for task in plan:
        print(f"{task.time} | {task.title} | Priority: {task.priority.capitalize()}")

    # Check conflicts
    conflicts = scheduler.detect_conflicts(plan)

    if conflicts:
        print("\n⚠️ Conflicts detected:")
        for t1, t2 in conflicts:
            print(f"- {t1.title} and {t2.title} at {t1.time}")
    else:
        print("\nNo conflicts detected.")


if __name__ == "__main__":
    main()