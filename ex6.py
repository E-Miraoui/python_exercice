# 1. Create an empty list
todo_list = []

# 2. Ask the user to enter three tasks
for i in range(1, 4):
    task = input(f"Enter task {i}: ")
    todo_list.append(task)

# 3. Display the full list of tasks
print("\nYour To-Do List:")
for idx, task in enumerate(todo_list, start=1):
    print(f"{idx}. {task}")

# 4. Ask which task has been completed
completed_task = input("\nWhich task have you completed? ")

# 5. Remove the completed task
if completed_task in todo_list:
    todo_list.remove(completed_task)
    print("\nTask removed successfully!")
else:
    print("\nTask not found in the list!")

# Display updated list
print("\nUpdated To-Do List:")
for idx, task in enumerate(todo_list, start=1):
    print(f"{idx}. {task}")

# 6. Sort the remaining tasks alphabetically and display
todo_list.sort()
print("\nSorted To-Do List:")
for idx, task in enumerate(todo_list, start=1):
    print(f"{idx}. {task}")
