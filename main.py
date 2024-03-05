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
            choice = input("Enter Your Choice:- ")
            if(choice) == '1':
                header = input("Enter Header of the Task ")
                description = input("Enter Description of the Task ")
                task = Task()
                task.header = header
                task.description = description
                print(task.__dict__)
        except Exception as e:
            print(f"Error on Main{e}")
    

if __name__ =="__main__":
    main()
