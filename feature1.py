import json
with open('list_of_tasks.json', 'w') as file:
    list_of_tasks = json.load(file)


def user_input():
    task_name = input("What's the task you need to do?")
    task_due_date = input("When is it due?")
    task_description = input("Please enter a description of your task if you want to")
    priority_level = input("On a scale of 1 to 10, what's its priority level? 10 being the most important")

    if priority_level not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        priority_level = input("Please enter a number between 1 and 10")

    status = input("""Please chose the status of the task: 
    1. To be started
    2. In progress
    3. Finished""")

    if status not in [1, 2, 3]:
        status = input("Please enter a number between 1, 2 and 3")


def add_task():
    user_input()
    list_of_tasks.append({"task name": task_name,
                          "task due date": task_due_date,
                          "task description": task_description,
                          "priority level": priority_level,
                          "status": status})

    return "Task added successfully!"

