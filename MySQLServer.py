#!/usr/bin/env python3
"""
This script connects to a MySQL server and creates a database named 'alx_book_store'.
If the database already exists, the script will not fail.
"""

import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password_here'  # <-- Replace with your actual MySQL root password
        )

        # Check if the connection was successful
        if connection.is_connected():
            cursor = connection.cursor()

            # Create the database (no SELECT or SHOW statements used)
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        # Handle any errors while connecting or executing
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Close the connection properly
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
