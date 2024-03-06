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
            if not self.ListOFtasks:
                print("No tasks available.")
            for item in self.ListOFtasks:
                print(item)
        except Exception as e:
            print(f"Exception While Printing List")
    def UpdateTask(self,name):
        try:
            task = Task()
            for item in self.ListOFtasks:
                if(item.header == name):
                    item.is_completed = True
                    print("Task Marked Completed successfully")
                    break
        except Exception as e:
            print(f"Exception While Updating Task {e}")
    def __init__(self):
        self.ListOFtasks = []
