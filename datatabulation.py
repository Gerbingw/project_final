# ticket_management.py

import sqlite3

def create_tables():
    try:
        connection = sqlite3.connect("ticket_database.db")
        cursor = connection.cursor()

        # Create tickets table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tickets (
                selected_ticket_type TEXT,
                selected_ticket_amount INTEGER,
                selected_package_type TEXT,
                selected_package_amount INTEGER,
                selected_ride_pass_type TEXT,
                selected_ride_pass_amount INTEGER,
                total_price INTEGER
            )
        ''')

        connection.commit()

    except sqlite3.Error as e:
        print(f"Error creating tables: {e}")

    finally:
        if connection:
            connection.close()

def create_connection():
    try:
        connection = sqlite3.connect("ticket_database.db")
        return connection
    except sqlite3.Error as e:
        print(e)
        return None

def insert_ticket_data(selected_ticket_type,selected_ticket_amount,selected_package_type,selected_package_amount,selected_ride_pass_type,selected_ride_pass_amount,total_price):
    try:
        connection = sqlite3.connect("ticket_database.db")
        cursor = connection.cursor()

        cursor.execute('''
            INSERT INTO tickets (
                selected_ticket_type,
                selected_ticket_amount,
                selected_package_type,
                selected_package_amount,
                selected_ride_pass_type,
                selected_ride_pass_amount,
                total_price
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''',)

        connection.commit()
        print("Ticket data inserted successfully!")

    except sqlite3.Error as e:
        print(f"Error inserting ticket data: {e}")

    finally:
        if connection:
            connection.close()

# Main Program
if __name__ == "__main__":
    create_tables()
    # Add other initialization or main program logic here
