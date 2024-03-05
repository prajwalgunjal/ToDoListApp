class TODoList:




def main():
    toDOList = TODoList()

    while True:
        try:
            print('\nTo-Do List Menu:')
            print('1. Add Task')
            print('2. Mark Task as Complete')
            print('3. Display Tasks')
            print('4. Quit')
            
        except Exception as e:
            print(f"Error on Main{e}")
    

if __name__ =="__main__":
    main()