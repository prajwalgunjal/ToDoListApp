from Task import Task
class TODoList:

    def add_task(self, header, description):
        try:
            #task = Task(header, description)
            task = Task()
            task.header = header
            task.description = description
            task.is_completed = False
            #print(task.__dict__)
            self.ListOFtasks.append(task)
            print(f'Task "{task}" added successfully.')
        except Exception as e:
            print(f"Exception while inserting to List {e}")

    def PrintList(self):
        try:
            task = Task()
            for item in self.ListOFtasks:
                print(item)
        except Exception as e:
            print(f"Exception While Printing List")


    def __init__(self):
        self.ListOFtasks = []
