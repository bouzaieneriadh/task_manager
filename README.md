# Task Manager (Python console application) - Version 2
**Author:** bouzaiene riadh 1glsiA

## Features
- **1 - Add a task**: asks for a title, rejects empty input.
- **2 - Display tasks**: shows all tasks with their number and status (To Do / Completed).
- **3 - Search for a task**: shows the tasks whose titles contain a keyword.
- **4 - Edit a task**: select a task by its number and replace its title.
- **5 - Delete a task**: select a task by its number, confirm (y/n), then remove it.
- **6 - Mark as completed**: select a task by its number and mark it as completed.
- **0 - Exit**: closes the program. Any other option displays an error message.

If a task number does not exist, a clear message is shown and the program keeps running.

## Git / GitHub workflow used

Each new feature was developed on its own branch, then integrated with a Pull Request
that was reviewed and merged into `main`:

| Branch | Feature |
|---|---|
| `feature-edit-task` | Edit a task |
| `feature-delete-task` | Delete a task |
| `feature-mark-completed` | Mark as completed |

## How to run
1. Open the project folder in Visual Studio Code.
2. Open `main.py`.
3. Click the **Run Python File** button.
4. Use the menu in the terminal: type a number and press Enter.
