# Student Planner — Project Plan

## 1. Project Overview
Student Planner is a web application that helps students manage academic tasks, deadlines, and study progress.

## 2. Project Goals
- Make academic tasks easy to organize.
- Help students remember deadlines.
- Show task completion status.
- Provide a simple and user-friendly interface.

## 3. Target Users
- University students
- College students
- Students who want to organize their studies

## 4. Core Features — Version 1
1. Create a task.
2. View the task list.
3. Set a task deadline.
4. Mark a task as completed.
5. Edit and delete tasks.
6. Display task status.

## 5. Out of Scope — Version 1
- AI-generated study schedules
- User accounts and authentication
- Social features
- Mobile applications
- Payment features

These features may be considered in future versions.

## 6. Quality Requirements
- The interface should be simple and understandable.
- Tasks should display accurate information.
- Inputs should be validated.
- Relevant functionality should have tests.

## 7. Initial Success Criteria
- A user can create and view tasks.
- A user can edit and delete tasks.
- A user can set deadlines.
- A user can mark tasks as completed.
- The main functionality passes relevant tests.

## 8. Development Principles
- Work on one GitHub Issue at a time.
- Follow AGENTS.md.
- Keep changes small and focused.
- Test implemented functionality.
- Update documentation when requirements change.
- ## Technology Stack

The Student Planner MVP will use the following technologies:

- HTML: Structure of the web pages.
- CSS: Styling and layout of the user interface.
- Python: Application logic.
- Flask: Web application framework.
- SQLite: Storage for academic tasks.
- pytest: Automated testing.

## Initial Architecture

The application will be a simple web application.

- The frontend will use HTML and CSS.
- Flask will handle requests and application logic.
- SQLite will store academic tasks.
- pytest will test the application's behavior.

## MVP Features

The first version will allow students to:

1. Create an academic task.
2. View their task list.
3. Edit a task.
4. Delete a task.
5. Set a deadline.
6. Mark a task as completed.

AI study recommendations and automatic task prioritization are future improvements and are not part of the initial MVP.

## Development Constraints

- Keep the application simple and beginner-friendly.
- Write automated tests for new behavior.
- Do not add dependencies without approval.
- Document setup and testing instructions.
Technology Choices and Rationale

Frontend: HTML and CSS

HTML defines the structure of the web pages, while CSS controls their appearance and layout. They are suitable for a beginner-friendly MVP and do not require an additional frontend framework.

Backend: Python and Flask

Python is readable and beginner-friendly. Flask provides a simple way to handle web requests and application logic without the complexity of a larger framework.

Data Storage: SQLite

SQLite stores academic tasks in a database file. It is suitable for a small MVP because it does not require a separate database server.

Testing: pytest

pytest makes it straightforward to write and run automated tests. It helps verify that application features behave as expected.

Architecture

The browser displays HTML and CSS pages. Flask receives requests and handles application logic. The application uses SQLite to store and retrieve tasks. pytest runs automated tests against the application.

Dependency Policy

The project will use the approved dependencies listed in requirements.txt. Additional dependencies require approval before installation.
