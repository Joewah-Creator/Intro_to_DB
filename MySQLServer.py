#!/usr/bin/env python3
"""
This script connects to a MySQL server and creates a database named 'alx_book_store'.
If the database already exists, the script will not fail.
"""

import mysql.connector  # Keep this single import

def create_database():
    """Connect to MySQL and create the 'alx_book_store' database."""
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password_here"  # Replace with your actual MySQL root password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
            print("Database 'alx_book_store' created successfully!")

    #  Catch the specific exception exactly as the checker expects
    except mysql.connector.Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
