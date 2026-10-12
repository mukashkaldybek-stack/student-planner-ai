Student Planner — Development Process

Task Management
	•	All development tasks are tracked using GitHub Issues.
	•	Work on one issue at a time.
	•	Read the issue and its acceptance criteria before starting.
	•	Keep changes small and focused.
	•	GitHub Issues are the canonical task backlog.

Team Roles
	•	Product Manager (PM): Reviews and clarifies each task before implementation. Follow _docs/team/pm.md.
	•	Software Engineer: Implements one groomed task at a time. Follow _docs/team/software-engineer.md.
	•	QA Engineer: Verifies the implementation against the acceptance criteria. Follow _docs/team/qa-engineer.md.

Orchestrator

The main session acts as the orchestrator. It coordinates the PM, Software Engineer, and QA Engineer. It does not groom tasks, implement features, or perform QA itself.

Development Workflow
	1.	Select the next open GitHub Issue.
	2.	PM reviews and grooms the issue before implementation.
	3.	Software Engineer implements the groomed task.
	4.	Software Engineer writes and runs relevant tests, commits the changes, and comments on the issue.
	5.	QA Engineer checks the implementation against every acceptance criterion and reports PASS or FAIL.
	6.	If QA reports FAIL, the Software Engineer addresses the reported problems and requests another QA review.
	7.	If QA reports PASS, the orchestrator closes the issue.
	8.	Repeat until the backlog is empty.

Rules
	•	Do not skip the PM grooming step.
	•	The Software Engineer must not change acceptance criteria or close the issue.
	•	QA must not fix code; QA only reports findings and PASS or FAIL.
	•	The orchestrator closes an issue only after QA reports PASS.
	•	Commit changes regularly.
	•	Do not add unapproved features or dependencies.

Documentation
	•	Follow AGENTS.md.
	•	Follow the requirements in _docs/plan.md.
	•	Update documentation when necessary.
