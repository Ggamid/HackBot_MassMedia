import psycopg2
from data.config import HOST, USER, DB_NAME, DB_PASSWORD


# Establish a connection to the PostgreSQL database
def create_bd():
    try:
        conn = psycopg2.connect(database=DB_NAME, user=USER, password=DB_PASSWORD, host=HOST)
    except psycopg2.Error as e:
        print("Error: Could not make connection to the PostgreSQL database.")
        print(e)

    # Create a cursor object
    cur = conn.cursor()

    # Define the SQL statement for creating a new table
    create_table_query = '''CREATE TABLE lots_table
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


def addLot(tg_id, lot_photo_id, text_lot, status_lot="Опубликовано", lot_video_id="-"):
    try:
        with psycopg2.connect(database=DB_NAME, user=USER, password=DB_PASSWORD, host=HOST) as con:
            with con.cursor() as cur:
                cur.execute(f"insert into lots_table(user_id, lot_photo_id, text_lot, status_lot,lot_video_id) Values(%s)", [tg_id, lot_photo_id, text_lot, status_lot, lot_video_id])

    except psycopg2.Error as _ex:
        print("[INFO]", _ex)



def drop_table():
    try:

        with psycopg2.connect(database=DB_NAME, user=USER, password=DB_PASSWORD, host=HOST) as con:
            con.autocommit = True
            with con.cursor() as cur:
                cur.execute("DROP TABLE lots_table")

    except Exception as e:
        print("[INFO] Error while working with PostgreSQL", e)


create_bd()