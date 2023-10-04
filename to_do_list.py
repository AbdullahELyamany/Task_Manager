"""
 Task Manager

 Created By *Abdullah EL-Yamany*

 Youtube Channel => Codezilla
 Video Link => https://youtu.be/xNm6y8SYcs4?si=-ABjUN4IluEg9sXg


Steps:-
 1- Add Tasks To a List
 2- Mark Task as Complete
 3- View Tasks
 4- Quit

"""

#from new_tasks import tasks

# ------------------ Variables ------------------- #
mesgs = """\033[;35;m
 1- Add Tasks To a List
 2- Mark Task as Complete
 3- View Tasks
 4- Quit"""

#tasks = []
tasks = [
    {"task":"Quran", "completed":False},
    {"task":"Salah", "completed":True}, 
    {"task":"Study", "completed":False},
    {"task":"Exercise", "completed":False}, 
    {"task":"Sleep", "completed":False},
    {"task":"Visit Hamada", "completed":True}
]

# ------------------ Functions ------------------- #

def main():
    # -------- Main Loop -------- #
    while True:
    
        print(mesgs)
    
        choice = input("\033[;39;mEnter Your Number Choice: ")
    
        if choice == "1":
            add_tasks()
        elif choice == "2":
            mark_task_complete()
        elif choice == "3":
            view_tasks(tasks)
        elif choice == "4":
            print("\033[;36;m\n\nThank You For Try")
            break
        else:
            print("\033[;31;mPlease Enter The Correct Number Between 1 : 4")


def add_tasks():
    # get task from user
    task = input("\033[;39;m\nEnter The New Task: ")
    note = input("\033[;39;mEnter a note related to this task: ")

    # define task status
    task_info = {"task": task, "completed": False, "note": note}

    # Add task to the list of tasks
    tasks.append(task_info)
    print("\033[;32;m\nTask Added To The List Successfully")


def mark_task_complete():
    # get list of incomplete tasks
    incomp_tasks = [task for task in tasks if task["completed"] == False]

    if len(incomp_tasks) == 0:
        print("\033[;31;mNo Tasks To Mark As Complete")
        return

    # show them to the user
    for i, task in enumerate(incomp_tasks, 1):
        print(f"\033[;35;m{i}- {task['task']}")

    try:
        # get the task from the user
        task_num = int(input("\033[;39;mChoose The Task Number to Complete: "))

        if task_num > 1 or task_num > len(incomp_tasks):
            #raise IndexError("Invalid Task Number")
            print("Invalid Task Number")
            return

    except ValueError:
        print("\033[;31;mInvalid Input, Please Enter A Number")
        return

    # mark the task as completed
    incomp_tasks[task_num-1]["completed"] = True

    # print a message to the user
    print(f"\033[;32;m{incomp_tasks[task_num-1]['task']}, Task Is Completed")

    if len(incomp_tasks) <= 1:
        print("\033[;32;m\nAll Tasks Is Completed")
        return

    incomp_tasks.remove(incomp_tasks[task_num-1])
    print("\033[;35;mTasks InComplete:")

    for i, task in enumerate(incomp_tasks, 1):
        #if i != task_num:
        print(f" {i}- {task['task']}")


def view_tasks(tasks):
    if not tasks:
        print("\033[;31;m\nThere Are No Tasks")
        return

    for i, task in enumerate(tasks, 1):
        status = "✔" if task["completed"] else "❌"
        print(f"\033[;35;m {i}- {task['task']} {status}")


if __name__ == "__main__" :

    main()
