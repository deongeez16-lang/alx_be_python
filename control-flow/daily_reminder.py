# daily_reminder.py - Python 3.8 compatible

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

if priority == "high":
    message = f"'{task}' is a high priority task"
elif priority == "medium":
    message = f"'{task}' is a medium priority task"
elif priority == "low":
    message = f"'{task}' is a low priority task"
else:
    message = f"'{task}' has an unknown priority level"

if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    message += ". Consider completing it when you have free time."

print("\nReminder:", message)

