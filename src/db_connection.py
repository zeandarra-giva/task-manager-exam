import pymysql
import sys

def get_db_connection():
    """
    Establishes a raw connection to the MySQL database.
    """
    try:
        connection = pymysql.connect(
            host='localhost',
            user='root',        
            # password='zeanzaeberche07081016', 
            password='YOUR_DB_PASSWORD', #change password here before running locally
            database='task_manager_db',
            cursorclass=pymysql.cursors.DictCursor
        )
        return connection
    except pymysql.MySQLError as e:
        print(f"Error connecting to MySQL: {e}")
        sys.exit(1)