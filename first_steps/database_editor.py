import string
from psycopg2 import connect

def execAndPrintQuery(cursor, query: string):
    cursor.execute(query)
    if ( query.split()[0] == "select" ):
        for row in cursor:
            print(row)

def closeConnection():
    print("Commiting changes and closing connection...")

def get_dsn():
    host   = input("Enter host: ")
    dbname = input("Enter dbname: ")
    user   = input("Enter user: ")
    passwd = input("Enter passwd: ")
#    if not host:
#        host = "/var/run/postgresql"
#    if not dbname:
#        dbname = "matej"
#    if not user:
#        user = "matej"  
    return "host={} dbname={} user={} password={}".format(host, dbname, user, passwd)

def print_menu():
    print("Hello this is your database script!")
 
def run(cur,conn):
    inp = ''
    while True:
        inp = input("Enter your query or q to quit:\n")
        if ( inp == 'q' ):
            closeConnection()
            return
        else:
            try:
                execAndPrintQuery(cur,inp)
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
