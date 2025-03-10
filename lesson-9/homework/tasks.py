import json
import csv

with open("tasks.json", "r") as file:
    tasks = json.load(file)

for task in tasks:
    print(f"ID: {task['id']}, Task: {task['task']}, Completed: {task['completed']}, Priority: {task['priority']}")

total = len(tasks)
completed = sum(1 for task in tasks if task["completed"])
pending = total - completed
avg_priority = sum(task["priority"] for task in tasks) / total

print(f"\nTotal tasks: {total}")
print(f"Completed tasks: {completed}")
print(f"Pending tasks: {pending}")
print(f"Average priority: {avg_priority:.2f}")


with open("tasks.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["ID", "Task", "Completed", "Priority"])
    for task in tasks:
        writer.writerow([task["id"], task["task"], task["completed"], task["priority"]])

print("Tasks saved to tasks.csv.")
