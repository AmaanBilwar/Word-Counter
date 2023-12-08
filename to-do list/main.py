def display_menu():
    print("to do list menu:")
    print("1. add task")
    print("2. display tasks")
    print("3. delete task")
    print("4. exit")

def add_tasks(task_list):
    task_name = input("enter the name of the task: ")
    task_list.append(task_name)

# def display_tasks(task_list):
#     print("Tasks:")
#     for index, task in enuerate(task_list, start=1): 
#         print(f"{index}. {task}")




def main():
    tasks = []  # Initialize an empty list to store tasks
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_tasks(tasks)
        # elif choice == "2":
        #     display_tasks(tasks)
        # Add conditions for other menu options (delete_task(), exit, etc.)
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")




