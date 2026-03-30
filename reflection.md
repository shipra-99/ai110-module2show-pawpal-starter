# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

The PawPal+ system is designed to help a pet owner manage daily pet care tasks efficiently. The system focuses on three core user actions:

1. Add and manage pets
2. Add and manage tasks for each pet (such as walks, feeding, medications)
3. Generate a daily schedule based on task priority and time

To support this, I designed the system using four main classes:

- **Owner**: Represents the user and stores multiple pets. It acts as the central access point for retrieving all tasks across pets.
- **Pet**: Represents an individual pet and stores its associated tasks.
- **Task**: Represents a single activity with attributes such as duration, priority, and scheduled time.
- **Scheduler**: Responsible for organizing tasks, generating the daily plan, and later handling sorting and conflict detection.

This design follows object-oriented principles by separating responsibilities clearly across classes.

**b. Design changes**


At this stage, the design is kept simple to avoid over-engineering. I focused only on the core entities required for the system. 

I may refine the Scheduler later to include more advanced logic such as conflict detection, filtering, and recurring tasks once the base system is working.

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
