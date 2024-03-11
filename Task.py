class Task:
    def __init__(self, header=None, description=None, is_completed=False):
        self.header = header
        self.description = description
        self.is_completed = False

    def __str__(self):
        return f'Task: {self.header}, Description: {self.description}, Completed: {self.is_completed}'
    def to_dict(self):
        return {
            'header': self.header,
            'description': self.description,
            'is_completed': self.is_completed
        }