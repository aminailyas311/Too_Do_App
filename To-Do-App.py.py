def task():
    tasks =[]
    print("------WELCOME TO TASK MANAGMENT APP-----")
    total_task=int(input("enter how many task you want to add: "))
    for i in range(1 , total_task+1):
       task_name = (input(f"enter task {i}: "))
       tasks.append(task_name)
    print(f"today's tasks are:\n{tasks}")


    while True:
        operation= int(input("enter:1-add\n2-update\n3-delete\n4-upgrade5-exit: "))
        if operation=="1":
            add = input("enter task you want to add:")
            tasks.append(add)
            print("task {add} has been succesfully added")
        elif operation=="2":
            update_value = input("enter the task you want to upgrade : ")
            if update_value in tasks:
                up=("enter new task=:")
                ind = tasks.index(update_value)
                tasks[ind]= up
                print("updated_tasks {up}")

task()