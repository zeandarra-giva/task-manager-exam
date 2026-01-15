from src.task import Task

class TaskManager:
    def __init__(self, db_connection):
        self.db=db_connection
        self.tasks=[]
        self.load_tasks_from_db()

    def load_tasks_from_db(self):
        with self.db.cursor() as cursor:
                    cursor.execute("SELECT * FROM tasks")
                    rows = cursor.fetchall()
                    self.tasks = []
                    for row in rows:
                        t = Task(row['id'], row['title'], row['description'],
                                row['due_date'], row['priority'], row['status'], row['created_at'])
                        self.tasks.append(t)      

    def add_task(self,title,description,due_date,priority):
          with self.db.cursor() as cursor:
                sql="INSERT INTO tasks (title,description,due_date, priority) VALUES (%s,%s,%s,%s)"
                cursor.execute(sql,(title, description,due_date,priority))
                self.db.commit()
                # Refresh our list
                self.load_tasks_from_db()

                print("Task added successfully")
    
    def list_task(self):
        # check if the tasks are empty first
        if not self.tasks:
            print("No task found")
        
        for t in self.tasks:
          print(f"{t.id}. {t.title} - {t.priority} ({t.status})")

    def update_task_status(self, task_id, new_status):
        with self.db.cursor() as cursor:
            sql = "UPDATE tasks SET status = %s WHERE id = %s"
            cursor.execute(sql, (new_status, task_id))
            self.db.commit()
            self.load_tasks_from_db() 
            print(f"Task {task_id} updated successfully.")

    def delete_task(self, task_id):
         with self.db.cursor() as cursor:
              sql="DELETE FROM tasks WHERE id=%s"
              cursor.execute(sql,(task_id,))
              self.db.commit()
              self.load_tasks_from_db()
              print(f"Task {task_id} deleted.")

          