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

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
