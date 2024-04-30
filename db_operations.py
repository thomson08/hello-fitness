# db_operations.py
import mysql.connector
from mysql.connector import Error

class DBOperations:
    def __init__(self, host="localhost", user="root", password="CPSC408!", database="RideShare2"):
        """Initialize the database connection."""
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        """Connect to the MySQL database."""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                auth_plugin='mysql_native_password'
            )
            if self.connection.is_connected():
                return self.connection
        except Error as e:
            print("Error while connecting to MySQL", e)
            return None

    def execute_query(self, query, params=None):
        """Execute a single query (INSERT, UPDATE, DELETE)."""
        result = None
        try:
            connection = self.connect()
            if connection:
                cursor = connection.cursor()
                cursor.execute(query, params)
                connection.commit()
                result = cursor.rowcount
                cursor.close()
        except Error as e:
            print(f"Error: {e}")
        finally:
            if connection.is_connected():
                connection.close()
        return result

    def fetch_data(self, query, params=None):
        """Fetch all rows from a query."""
        try:
            connection = self.connect()
            if connection:
                cursor = connection.cursor()
                cursor.execute(query, params)
                result = cursor.fetchall()
                cursor.close()
                return result
        except Error as e:
            print(f"Error: {e}")
        finally:
            if connection.is_connected():
                connection.close()

    def fetch_one(self, query, params=None):
        """Fetch a single row from a query."""
        try:
            connection = self.connect()
            if connection:
                cursor = connection.cursor()
                cursor.execute(query, params)
                result = cursor.fetchone()
                cursor.close()
                return result
        except Error as e:
            print(f"Error: {e}")
        finally:
            if connection.is_connected():
                connection.close()

# Example usage within the application
if __name__ == "__main__":
    db = DBOperations()
    insert_query = "INSERT INTO Users (username, password) VALUES (%s, %s)"
    db.execute_query(insert_query, ("testuser", "password123"))

    select_query = "SELECT * FROM Users WHERE username = %s"
    user = db.fetch_one(select_query, ("testuser",))
    print(user)
