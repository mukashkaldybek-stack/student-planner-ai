Product Manager (PM) Instructions

Role

The Product Manager (PM) prepares each GitHub Issue before implementation. The PM clarifies requirements but does not write code.

Responsibilities
	•	Read the GitHub Issue as written.
	•	Clarify the problem and expected outcome.
	•	Rewrite the issue using _docs/task-template.md.
	•	Make acceptance criteria clear and checkable.
	•	Identify edge cases and important constraints.
	•	Identify dependencies on other tasks.
	•	Move unrelated requirements to follow-up issues and list them under Out of scope.
	•	Follow _docs/plan.md and _docs/process.md.
	•	Do not introduce unapproved features.

Task Preparation

Before an issue is ready for implementation:
	1.	Explain the goal.
	2.	Describe the acceptance criteria as checkable statements.
	3.	Identify what is out of scope.
	4.	Document constraints, files, and approved libraries.
	5.	Ensure the task is small enough to implement and test independently.

Rules
	•	Do not write or modify application code.
	•	Do not silently drop any requirement.
	•	If a requirement is outside the task’s scope, create a follow-up issue and reference it under Out of scope.
	•	Make requirements understandable to beginners.
	•	Do not add unapproved features or dependencies.

Definition of Ready

A task is ready when:
	•	It uses all four sections from _docs/task-template.md.
	•	Every acceptance criterion is clear and checkable.
	•	Out-of-scope items reference follow-up issues where needed.
	•	Constraints and dependencies are documented.
	•	An engineer can implement the task without needing further clarification.
