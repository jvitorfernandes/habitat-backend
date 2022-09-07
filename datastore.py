import sqlite3


def create_table():
    connection = sqlite3.connect('datastore.db')
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Datastore
        (id INTEGER, 
        company TEXT, 
        unit_name TEXT,
        efa_date TEXT,
        delivery_start TEXT,
        delivery_end TEXT,
        efa INTEGER,
        service TEXT,
        cleared_volume INTEGER,
        cleared_price INTEGER,
        technology_type TEXT,
        location TEXT,
        Cancelled TEXT)
        ''')

    connection.commit()
    connection.close()


def load_table(results):
    connection = sqlite3.connect('datastore.db')
    cursor = connection.cursor()

    results_values = [list(result.values()) for result in results]

    cursor.executemany('INSERT INTO Datastore VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)', results_values)

    # records = cursor.execute("SELECT * FROM Datastore")
    # # print(cursor.fetchall())
    #
    # for record in records:
    #     print(record)

    connection.commit()
    connection.close()

