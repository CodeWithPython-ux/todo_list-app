tasks = []

while True:

    print("\n===== TO DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        task = input("Enter Task: ")
        tasks.append(task)

        print("Task Added Successfully!")

    elif choice == "2":

        if len(tasks) == 0:
            print("No Tasks Available")

        else:
            print("\nYour Tasks:")

            count = 1

            for task in tasks:
                print(count, ".", task)
                count += 1

    elif choice == "3":

        if len(tasks) == 0:
            print("No Tasks To Delete")

        else:
            print("\nYour Tasks:")

            count = 1

            for task in tasks:
                print(count, ".", task)
                count += 1

            task_no = int(input("Enter Task Number To Delete: "))

            if task_no >= 1 and task_no <= len(tasks):

                tasks.pop(task_no - 1)

                print("Task Deleted Successfully!")

            else:
                print("Invalid Task Number")

    elif choice == "4":

        print("Good Bye!")
        break

    else:

        print("Invalid Choice")