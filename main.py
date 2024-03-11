from ToDOList import TODoList
from Task import Task


def main():
    toDOList = TODoList()
    #task = Task()
    while True:
        try:
            print('\nTo-Do List Menu:')
            print('1. Add Task')
            print('2. Mark Task as Complete')
            print('3. Display Tasks')
            print('4. Quit')
            choice = int(input("Enter Your Choice:- "))
            if(choice) == 1:
                header = input("Enter Header of the Task ")
                description = input("Enter Description of the Task ")
                toDOList.add_task(header,description)
                toDOList.save_json()
            elif(choice) == 2:
                name = input("Enter name of the Task which You want to mark as completed ")
                toDOList.UpdateTask(name)
            elif(choice) == 3:
                toDOList.PrintList()
            elif(choice) == 4 :
                print("Existing From Program Thank You ")
                break
            else:
                print("Invalid choice. Please choose a valid option.")
        except Exception as e:
            print(f"Invalid input. Please enter a number {e}")
    

if __name__ =="__main__":
    main()
