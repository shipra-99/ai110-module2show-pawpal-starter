# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

The PawPal+ system is designed using four main classes: Owner, Pet, Task, and Scheduler.

- **Owner**: Represents the user and stores multiple pets. It acts as the central point to retrieve all tasks across pets.
- **Pet**: Represents an individual pet and maintains a list of tasks associated with that pet.
- **Task**: Represents a single activity such as feeding, walking, or medication. It includes attributes like duration, priority, time, and completion status.
- **Scheduler**: Responsible for organizing tasks and generating a daily plan. It will handle sorting, prioritization, and conflict detection.

This design separates responsibilities clearly. Each class has a single role, which makes the system modular and easier to extend later.

**b. Design changes**

**b. Design changes**

After reviewing the initial design, I ensured that the Scheduler class is responsible only for planning logic and does not store any task data directly. Instead, it retrieves tasks from the Owner, which aggregates tasks from all pets.

This separation avoids tight coupling between classes and keeps the system flexible and scalable. It ensures that changes to pets or tasks do not require modifications to the scheduling logic.

I also refined the data flow so that all task retrieval happens through the Owner class. This creates a single source of truth and prevents inconsistencies when accessing tasks across multiple pets.

Additionally, I confirmed that relationships are properly defined:
- Owner contains multiple pets
- Each pet contains multiple tasks
- Scheduler interacts with Owner to access all tasks

No major structural changes were needed, but this review helped validate that the design is clean, maintainable, and ready for future extensions such as filtering, recurring tasks, and conflict detection.
---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

**b. Tradeoffs**

One tradeoff in my scheduler design is that conflict detection only checks for tasks scheduled at the exact same time, rather than detecting overlapping durations. For example, if one task is from 09:00–09:30 and another starts at 09:15, this overlap would not be detected.

This approach was chosen to keep the algorithm simple and efficient (O(n) time complexity using a dictionary). While more advanced overlap detection could be implemented, it would increase complexity and reduce readability.

Additionally, I chose a more readable implementation for conflict detection instead of a more compact “Pythonic” version suggested by AI. While the alternative used advanced constructs like defaultdict and list comprehensions, I prioritized clarity and maintainability for this project.

---

## 3. AI Collaboration

**a. How you used AI**

I used AI tools like Copilot for multiple parts of the project, including initial design brainstorming, generating class skeletons, implementing scheduling logic, and debugging errors. It was especially helpful for quickly drafting methods like sorting tasks using `sorted()` and understanding how to structure interactions between classes like Owner, Pet, and Scheduler.

The most helpful prompts were specific and task-focused, such as asking how the Scheduler should retrieve tasks from the Owner, or how to implement filtering and conflict detection efficiently. Breaking the work into phases and asking targeted questions helped me get better and more relevant responses.

---

**b. Judgment and verification**

One instance where I did not accept an AI suggestion as-is was in the conflict detection logic. Copilot suggested a more compact implementation using advanced Python features like `defaultdict` and list comprehensions. While it worked, I found it less readable and harder to understand.

I evaluated the suggestion by comparing it with my simpler dictionary-based approach and decided to keep my version because it was clearer and easier to maintain. I also verified correctness by testing it through both the CLI demo (`main.py`) and automated tests using pytest.


---

## 4. Testing and Verification

**a. What you tested**

I tested core behaviors of the system, including task completion, task addition, sorting by time, filtering out completed tasks, recurring task generation, and conflict detection. I also included edge cases such as having no tasks and having multiple tasks at the same time.

These tests were important to ensure that the scheduler behaves correctly under both normal and edge conditions, and that the algorithmic logic (sorting, filtering, recurrence) works as expected.


**b. Confidence**

I am confident in the correctness of my scheduler (around 4 out of 5). The core features work reliably and are covered by automated tests. The system correctly handles sorting, filtering, recurrence, and conflict detection.

If I had more time, I would test more complex edge cases such as overlapping task durations (not just exact time matches), multiple pets with many tasks, and more advanced recurrence scenarios involving actual dates instead of simple repetition.


---

## 5. Reflection

**a. What went well**

The part I am most satisfied with is the Scheduler design. It cleanly separates logic for sorting, filtering, recurrence, and conflict detection, making the system modular and easy to extend. I was also able to successfully integrate backend logic with the Streamlit UI, which made the application feel complete.

**b. What you would improve**

If I had another iteration, I would improve how time and scheduling are handled by using proper datetime objects instead of strings. I would also redesign the Task class to directly associate tasks with specific pets instead of relying on indirect filtering, and enhance the UI to allow users to input task times and frequencies more flexibly.


**c. Key takeaway**

One key takeaway from this project is that even when using powerful AI tools, the developer still needs to act as the system architect. AI can generate useful code and ideas, but it is important to evaluate those suggestions critically and prioritize clarity, correctness, and maintainability. The best results came from treating AI as a collaborator rather than relying on it blindly.