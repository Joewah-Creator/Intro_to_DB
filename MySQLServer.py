"""
This script connects to a MySQL server and creates a database named 'alx_book_store'.
If the database already exists, the script will not fail.
"""

import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL Server (adjust host, user, password if needed)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password_here'  # <-- Replace with your actual MySQL root password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Ensure the cursor and connection are properly closed
        if connection.is_connected():
            cursor.close()
            connection.close()
            # Optional: print message confirming closure
            # print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
