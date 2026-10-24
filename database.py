# database.py
import mysql.connector

# DATABASE CONNECTION

def get_connection():

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Shristy@1227",
        database="digital_wellbeing"
    )

    return connection

# EXECUTE INSERT / UPDATE / DELETE

def execute_query(query, values=None):

    connection = get_connection()
    cursor = connection.cursor()

    try:

        cursor.execute(query, values)

        connection.commit()

        return cursor.lastrowid

    except mysql.connector.Error as error:

        print("\nDatabase Error:", error)

        connection.rollback()

        return None

    finally:

        cursor.close()
        connection.close()

# FETCH ONE RECORD

def fetch_one(query, values=None):

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    try:

        cursor.execute(query, values)

        return cursor.fetchone()

    except mysql.connector.Error as error:

        print("\nDatabase Error:", error)

        return None

    finally:

        cursor.close()
        connection.close()


# =========================================================
# FETCH MULTIPLE RECORDS
# =========================================================

def fetch_all(query, values=None):

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    try:

        cursor.execute(query, values)

        return cursor.fetchall()

    except mysql.connector.Error as error:

        print("\nDatabase Error:", error)

        return []

    finally:

        cursor.close()
        connection.close()