import mysql.connector
from mysql.connector import errorcode

# Configuration for the target database and connection
DB_NAME = "alx_book_store"
CONFIG = {
    # NOTE: Replace 'your_password' and potentially 'root' 
    # with your actual MySQL server credentials.
    'user': 'root',
    'password': 'Oghena&#Ogie!', 
    'host': '127.0.0.1' 
}

def create_database():
    """
    Connects to the MySQL server and creates the specified database. 
    Handles connection errors and ensures the connection is closed.
    """
    cnx = None  # Initialize connection variable
    cursor = None # Initialize cursor variable

    try:
        # Step 5: Handle open (Attempt connection)
        print(f"Attempting to connect to MySQL server at {CONFIG['host']}...")
        cnx = mysql.connector.connect(**CONFIG)
        cursor = cnx.cursor()
        print("Successfully connected to MySQL server.")

        # Step 6: Execute the SQL statement
        # Using 'CREATE DATABASE IF NOT EXISTS' ensures the script does not fail
        sql_query = f"CREATE DATABASE IF NOT EXISTS {DB_NAME}"
        cursor.execute(sql_query)
        
        # Required print message on success
        print(f"Database '{DB_NAME}' created successfully!")

    # Step 7: Handle Connection Errors
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("\nError connecting to DB: Access denied! Check your MySQL username and password in the script.")
        else:
            # Print error message for other connection failures
            print(f"\nError connecting to DB: {err}")
            
    # Step 8: Handle close (Cleanup)
    finally:
        if cursor is not None:
            cursor.close()
        if cnx is not None and cnx.is_connected():
            cnx.close()
            # print("MySQL connection closed.") # Optional confirmation

if __name__ == "__main__":
    create_database()