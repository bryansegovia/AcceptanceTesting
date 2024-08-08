class ToDoListManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Add a new task to the to-do list."""
        self.tasks.append({'task': task, 'completed': False})

    def list_tasks(self):
        """List all the tasks in the to-do list."""
        for idx, task in enumerate(self.tasks, start=1):
            status = 'Completed' if task['completed'] else 'Pending'
            print(f"{idx}. {task['task']} - {status}")

    def mark_task_completed(self, task_number):
        """Mark a task as completed."""
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]['completed'] = True
        else:
            print("Invalid task number.")

    def clear_tasks(self):
        """Clear the entire to-do list."""
        self.tasks.clear()

    # Nueva funcionalidad
    def mark_all_tasks_completed(self):
        """Mark all tasks as completed."""
        for task in self.tasks:
            task['completed'] = True

# Example usage:
if __name__ == "__main__":
    manager = ToDoListManager()
    manager.add_task("Buy groceries")
    manager.add_task("Read a book")
    manager.add_task("Go for a walk")
    manager.list_tasks()
    manager.mark_task_completed(1)
    manager.list_tasks()
    manager.mark_all_tasks_completed()
    manager.list_tasks()
    manager.clear_tasks()
    manager.list_tasks()