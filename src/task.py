import datetime as dt

class Task:

    def __init__(self, task_id, title, description, due_date, priority, status, created_at=None):
        self.id=task_id
        self.title=title
        self.description=description
        self.due_date=due_date
        self.priority=priority
        self.status=status
        self.created_at=created_at or dt.datetime.now()
 
    def __str__(self):
        return f"[{self.id}] {self.title} | Status: {self.status} | Priority: {self.priority}"