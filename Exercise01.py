list=[]
print("Insert the action correspongin to the number you want to perform:\n1)Insert a new task\n2)Remove a task\n3)"
      "show all existing tasks\n4)Close the program")
j=1
while j != 0:
    choice=int(input("Your choice: "))
    if choice==1:
        new_task=input("Insert new task: ")
        list.append(new_task)
    elif choice==2:
        del_task=input("Delete the task: ")
        list.remove(del_task)
    elif choice==3:
        print(list)
    else:
        j=0

