TOKEN = "6132503251:AAG6XaMYcqDyoDJ7xLWSRT0eoZcMAPzz9ho"
HOST = "127.0.0.1"
USER = "gamid"
DB_PASSWORD = "kt7c2YJB"
DB_NAME = "gamidkhalidov"
import psycopg2


def create_bd():
    try:
        conn = psycopg2.connect(database=DB_NAME, user=USER, password=DB_PASSWORD, host=HOST)
    except psycopg2.Error as e:
        print("Error: Could not make connection to the PostgreSQL database.")
        print(e)

    # Create a cursor object
    cur = conn.cursor()

    # Define the SQL statement for creating a new table
    create_table_query = '''CREATE TABLE if not exist lots_table
                (lot_photo_id TEXT,
                 lot_video_id TEXT,
                 user_id INTEGER,
                 status_lot TEXT,
                 text_lot TEXT);'''

    # Execute the SQL statement
    try:
        cur.execute(create_table_query)
        conn.commit()
        print("Table created successfully.")
    except psycopg2.Error as e:
        print("Error: Could not create the table.")
        print(e)

    # Close the cursor and connection
    cur.close()
    conn.close()
