def addTask():
    task=input("Enter your task: ")
    list.append(task)
    print(f"Your task '{task}' has been added to the list.")
    print("----------------------------------------------")
    print("\n")

def delTask():
    task=input("Enter the task to be deleted: ")
    if task in list:
        list.remove(task)
        print(f"Your task '{task}' ahs been removed from the list.")
    else:
        print(f"Your task '{task}' was not found on the list.")
    print("--------------------------------------------")
    print("\n")

def listTask():
    if not list:
        print("You don't have any tasks.")
    else:
        print("Your tasks are:\n")
        for tasks in list:
            print(tasks)
    print("--------------------------------------------")
    print("\n")


list=[]

while True:
    print("Welcome! what would you like to do today?")
    print("1. Add a task to your list.")
    print("2. Delete a task from list.")
    print("3. List")
    print("4. Exit")
    print("---------------------------------")
    n=input("PLease select a task from above: ")
    if n=="1":
        addTask()
    elif n=="2":
        delTask()
    elif n=="3":
        listTask()
    elif n=="4":
        break
    else:
        print("Invalid Choice. Please try again.")
        print("---------------------------------")
    print("\n")