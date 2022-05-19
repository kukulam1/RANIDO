import sqlite3
from sqlite3 import Error
from sys import stderr

# Connect to database, create it if it does not exists
def connection_init():
    connection = None
    try:
        connection = sqlite3.connect('company.db')
    except Error as e:
        print(e)
    return connection

# Select records
def select_records( cursor ):
    to_select = input('Columns: ')
    table = input('Select table: ')
    sql = f'SELECT ' + to_select + ' FROM ' + table
    cursor.execute(sql)
    print( cursor.fetchall() )

# Commit changes into database
def commit_changes( connection ):
    connection.commit()
    print("Changes commited.")

# Delete record from table
def delete_record( cursor ):
    table = input('Select table: ')
    id = input('Select ID: ')
    sql = f'DELETE FROM ' + table + ' WHERE id=?'
    cursor.execute(sql, id)
    print("Delete record.")

# Update record in table
def update_record( cursor ):
    table = input('Select table: ')
    to_update = input('Columns to update: ')
    where = input('Where:')
    sql = f'UPDATE ' + table + ' SET ' + to_update + ' WHERE ' + where
    cursor.execute(sql)
    print("Update record.")    

# Insert record into table
def insert_record( cursor ):
    table = input('Select table: ')
    value = input('What to insert: ')
    sql = f'INSERT INTO ' + table + ' VALUES ' + value
    cursor.execute(sql)
    print("Insert record.")   

def print_menu():
    print("Menu:\ns..select\ni..insert\nd..delete\nu..update\nc..commit changes\nq..your own sql query\ne..exit\n")

def main():

    connection = connection_init()
    cursor = connection.cursor()
    print_menu()

    try:
        while (True):
            option = input('company.db> ')
            match option:
                case 's':
                    select_records( cursor )
                case 'i':
                    insert_record( cursor )
                case 'd':
                    delete_record( cursor )
                case 'u':
                    update_record( cursor )
                case 'c':
                    commit_changes( connection )
                case 'q':
                    query = input('Enter your query:')
                    cursor.execute( query )
                case 'e':
                    break
    except Error as e:
        print( e, stderr)

    connection.close()

if __name__ == '__main__':
    main()