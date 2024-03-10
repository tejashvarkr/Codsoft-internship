# To Do List Initialize an empty list to store tasks
tasks = []

def show_list():

  if tasks:
    for i, task in enumerate(tasks):
      print(f"{i+1}. {task}")
  else:
    print("No tasks in the list!")

def add_task(task):
  
  tasks.append(task)
  print(f"Task '{task}' added!")

def remove_task(index):

  if index < 1 or index > len(tasks):
    print("Invalid task index!")
    return
  task = tasks.pop(index-1)
  print(f"Task '{task}' removed!")

def check_task(index):

  if index < 1 or index > len(tasks):
    print("Invalid task index!")
    return
  tasks[index-1] = f"[DONE] {tasks[index-1]}"
  print(f"Task '{tasks[index-1]}' marked as completed!")

def main():

  print("Welcome to your To-Do List App!")
  while True:
    print("\nOptions:")
    print("1. Show list")
    print("2. Add task")
    print("3. Remove task")
    print("4. Mark task as completed")
    print("5. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
      show_list()
    elif choice == "2":
      task = input("Enter task name: ")
      add_task(task)
    elif choice == "3":
      index = int(input("Enter task index to remove: "))
      remove_task(index)
    elif choice == "4":
      index = int(input("Enter task index to mark completed: "))
      check_task(index)
    elif choice == "5":
      print("Goodbye!")
      break
    else:
      print("Invalid choice!")

# Run the main program

if __name__ == "__main__":
  main()
