import pymysql

def get_db_info():
    try:
        db_conn = pymysql.connect(host="localhost", user="root", password="root123", database="my_literature")
        print("Connected to the database.")
        return db_conn
    except pymysql.MySQLError as e:
        print(f"Error connecting to the database: {e}")

def all_info():
    db_conn = get_db_info()
    if db_conn:
        try:
            query = "SELECT * FROM books"
            comm_channel = db_conn.cursor()
            comm_channel.execute(query)
            result = comm_channel.fetchall()
            print(result)
        except pymysql.MySQLError as e:
            print(f"Error executing query: {e}")
        finally:
            comm_channel.close()
            db_conn.close()

# Call the function to get all info
all_info()
