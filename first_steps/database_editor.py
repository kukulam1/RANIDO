import string
from psycopg2 import connect

def exec_query(cursor, query: string):
    cursor.execute(query)
    if ( query.split()[0] == "select" ):
        print_query(cursor)

def close_connection():
    print("Commiting changes and closing connection...")

def get_dsn():
    host   = input("Enter host: ")
    dbname = input("Enter dbname: ")
    user   = input("Enter user: ")
    passwd = input("Enter passwd: ")
    return "host={} dbname={} user={} password={}".format(host, dbname, user, passwd)

def print_menu():
    print("Hello this is your database script!")

def print_query(cursor):
    for row in cursor:
        print(row)
def run(cur,conn):
    inp = ''
    while True:
        inp = input("Enter your query or q to quit:\n")
        if ( inp == 'q' ):
            close_connection()
            return
        else:
            try:
                exec_query(cur,inp)
            except:
                print("Could not resolve your query!")
                conn.rollback()

def connection_init():
    dsn = get_dsn()
    try:
        conn = connect(dsn)
    except:
        print("Could not connect to PostrgreSQL!")
        return None, None
    cur = conn.cursor()
    return conn, cur
    
def main():
    print_menu()
    conn, cur = connection_init()
    if ( conn == None ):
        return
    run(cur,conn)
    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    main()
