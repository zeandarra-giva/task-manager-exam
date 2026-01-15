import sys
from src.db_connection import get_db_connection as db_connection
from src.task_manager import TaskManager as tm

def show_menu():
    print("\n=== Pick a Choice for Task Manager ===")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Update Task Status") 
    print("4. Delete Task")
    print("5. Exit")
    
def main():
    # Connect to db first
    print("Connecting to Database...")

    # Create objects
    db = db_connection()
    manager = tm(db)

    # Show Menu Options
    while True:
        show_menu()
        choice = input("\nSelect Option: ")

        if choice == "1":
            print("\nAdd Your Task:")
            title=input("Title: ")
            desc=input("Description: ")
            date=input("Due Date (YYYY-MM-DD): ")
            prio=input("Priority (Low/Medium/High): ")
            manager.add_task(title, desc, date, prio)
        elif choice == "2":
            print("\nHere are your current tasks: ")
            manager.list_task()
        elif choice == "3":
            manager.list_task() 
            print("---")
            t_id = input("\nEnter Task ID to update: ")
            new_status = input("Enter New Status (Pending/In Progress/Completed): ")
            manager.update_task_status(t_id, new_status)
        elif choice == "4":
            t_id_removed=input("Task ID to delete: ")
            manager.delete_task(t_id_removed)
        elif choice == "5":
            print("Thank you for using the app. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()