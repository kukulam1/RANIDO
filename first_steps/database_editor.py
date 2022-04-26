import string
import psycopg2

def ExecAndPrintQuery(cursor, query: string):
    cursor.execute(query)
    for row in cursor:
        print(row)

def Insert():
    print("Insert")

def getSelect():
    columns = input("What columns you want to select?\n")
    table  = input("From what talbe you want to select?\n")
    return "SELECT " + columns + " FROM " + table + ';'

def closeConnection():
    print("Closing connection...")

def getDsn(passwd: string, host = "/var/run/postgresql",
           dbname = "matej", user = "matej" ):
        return "host={} dbname={} user={} password={}".format(host, dbname, user, passwd)

def printMenu():
    print("Hello this is your database script!")
    print("Commands: i (INSERT) | s (SELECT) | q (quit).")
 
def run(cursor):
    inp = ''
    while inp != 'q':
        inp = input()
        if   inp == 'i':
            Insert(cursor)
        elif inp == 's':
            query = getSelect()
            ExecAndPrintQuery(cursor,query)
        elif inp == 'q':
            closeConnection()
            return
        else:
            print("Wrong option, try again.")
            
def main():
    passwd = input("Type your password:")
    dsn = getDsn(passwd)
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()
    printMenu()
    run(cur)
    cur.close()
    conn.close()

if __name__ == "__main__":
    main()
