import json
import os
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
            self.save_json()
            print(f'Task "{task}" added successfully.')
        except Exception as e:
            print(f"Exception while inserting to List {e}")

    def PrintList(self):
        try:
            task = Task()
            # if not self.ListOFtasks:
            #     print("No tasks available.")
            file_path = r'D:\PythonProjects\ToDOList\Task.json'
            with open(file_path, 'r') as json_file:
                data = json.load(json_file)
                for task_data in data:
                    task = Task(**task_data)
                    self.ListOFtasks.append(task)
            for item in self.ListOFtasks:
                print(item)
        except Exception as e:
            print(f"Exception While Printing List")
    def UpdateTask(self,name):
        try:
            for item in self.ListOFtasks:
                if(item.header == name):
                    item.is_completed = True
                    print("Task Marked Completed successfully")
                    break
        except Exception as e:
            print(f"Exception While Updating Task {e}")

    def save_json(self):
        try:
            file_path = r'D:\PythonProjects\ToDOList\Task.json'

            with open(file_path, 'r') as json_file:
                data = json.load(json_file)
                for task_data in data:
                    task = Task(**task_data)
                    self.ListOFtasks.append(task)
            contacts_as_dict = [task.to_dict() for task in self.ListOFtasks]
            with open(file_path, 'w') as json_file:
                json.dump(contacts_as_dict, json_file, indent=2)
                print("Tasks stored as JSON in 'Task.json'")
        except Exception as e:
            print(f"Exception: {e}")


    def __init__(self):
        self.ListOFtasks = []

