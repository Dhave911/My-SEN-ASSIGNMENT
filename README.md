# Library Book Borrowing System

This project is a simple implementation of a Library Book Borrowing System using Python's Object-Oriented Programming (OOP) principles. It was developed as part of the SEN 201 assignment.

## Software Development Life Cycle (SDLC)

The development of this project followed the traditional SDLC phases:

### 1. Planning
- **Objective**: Create a simple system to manage books and member borrowings.
- **Scope**: Define core entities like Books, Members, and the Library itself.
- **Feasibility**: Using Python for its simplicity and readability.

### 2. Requirement Analysis
- The system must allow adding books to the inventory.
- The system must register members.
- Members should be able to borrow available books.
- Members should be able to return books they have borrowed.
- The system should track the availability of each book.

### 3. Design
- **Entities**:
    - `Book`: Attributes include `title`, `author`, `isbn`, and `is_available`.
    - `Member`: Attributes include `name`, `member_id`, and a list of `borrowed_books`.
    - `Library`: Methods to `add_book`, `register_member`, `borrow_book`, and `return_book`.
- **Nomenclature**: The names used in the implementation (e.g., `Book`, `Member`, `Library`, `borrow_book`) match the design specifications.

### 4. Implementation
- The project was implemented in Python using classes to represent the entities defined in the design phase.
- Logic was added to handle borrowing and returning books, including validation checks for availability and member existence.

### 5. Testing
- Unit tests were conducted by simulating a library environment:
    - Adding books.
    - Registering a member.
    - Borrowing a book and verifying its status.
    - Attempting to borrow an already borrowed book.
    - Returning a book and verifying its status.

### 6. Deployment & Maintenance
- The code is pushed to a GitHub repository for submission.
- Future maintenance would involve adding features like due dates, fines, and a database for persistent storage.

## How to Run
1. Run the "Hello World" task:
   ```bash
   python hello.py
   ```
2. Run the Library System:
   ```bash
   python library_system.py
   ```
