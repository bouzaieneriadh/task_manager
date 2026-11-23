"""Task Manager - Version 2 (console application).

Features: add, display (To Do / Completed), search, edit, delete,
mark as completed.
"""

tasks = []  # each task is a dict: {"title": str, "done": bool}


def show_menu():
    print()
    print("=== TASK MANAGER ===")
    print("1. Add a task  2. Display  3. Search")
    print("4. Edit  5. Delete  6. Mark as completed  0. Exit")


def ask_task_number():
    """Ask for a task number; return its index, or None if invalid."""
    if len(tasks) == 0:
        print("No tasks yet.")
        return None
    raw = input("Task number: ").strip()
    if not raw.isdigit():
        print("Error: please enter a valid number.")
        return None
    number = int(raw)
    if number < 1 or number > len(tasks):
        print(f"Error: task {number} does not exist.")
        return None
    return number - 1


def status_text(task):
    return "Completed" if task["done"] else "To Do"


def add_task():
    title = input("Task title: ").strip()
    if title == "":
        print("Error: the title cannot be empty.")
        return
    tasks.append({"title": title, "done": False})
    print("Task added successfully.")


def display_tasks():
    if len(tasks) == 0:
        print("No tasks yet.")
        return
    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task['title']} [{status_text(task)}]")


def search_tasks():
    keyword = input("Keyword: ").strip().lower()
    if keyword == "":
        print("Error: the keyword cannot be empty.")
        return
    found = False
    for number, task in enumerate(tasks, start=1):
        if keyword in task["title"].lower():
            print(f"{number}. {task['title']} [{status_text(task)}]")
            found = True
    if not found:
        print("No task found.")


def edit_task():
    index = ask_task_number()
    if index is None:
        return
    new_title = input("New title: ").strip()
    if new_title == "":
        print("Error: the title cannot be empty.")
        return
    tasks[index]["title"] = new_title
    print("Task updated successfully.")


def delete_task():
    index = ask_task_number()
    if index is None:
        return
    answer = input(f"Delete '{tasks[index]['title']}'? (y/n): ").strip().lower()
    if answer == "y":
        tasks.pop(index)
        print("Task deleted.")
    else:
        print("Deletion cancelled.")


def complete_task():
    index = ask_task_number()
    if index is None:
        return
    if tasks[index]["done"]:
        print("This task is already completed.")
        return
    tasks[index]["done"] = True
    print("Task marked as completed.")


def main():
    running = True
    while running:
        show_menu()
        choice = input("Your choice: ").strip()
        if choice == "1":
            add_task()
        elif choice == "2":
            display_tasks()
        elif choice == "3":
            search_tasks()
        elif choice == "4":
            edit_task()
        elif choice == "5":
            delete_task()
        elif choice == "6":
            complete_task()
        elif choice == "0":
            print("Goodbye!")
            running = False
        else:
            print("Error: invalid option. Please choose 0 to 6.")


if __name__ == "__main__":
    main()