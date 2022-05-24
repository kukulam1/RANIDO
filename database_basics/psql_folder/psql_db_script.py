import string
import subprocess
from psycopg2 import connect
from psycopg2 import Error
from sys import stderr

# Connect to database
def connection_init():
    passwd = input("Enter password: ")
    dsn = f'host=localhost dbname=testdb user=matej password={passwd}'
    return connect(dsn)

# Select records
def select_records( cursor, table='people'):
    sql = f'SELECT * FROM {table}'
    cursor.execute(sql)
    for row in cursor:
        print(row)

# Commit changes into database
def commit_changes( connection ):
    connection.commit()
    print("Changes commited.")

# Delete record from table
def delete_record( cursor, table='people', id=1):
    sql = f'DELETE FROM {table} WHERE id={id}'
    cursor.execute(sql, id)
    print("Delete record.")

# Update record in table
def update_record( cursor, table='people', set='name=\'newbie\'', id='id=5' ):
    sql = f'UPDATE {table} SET {set} WHERE {id}'
    cursor.execute(sql)
    print("Update record.")    

# Insert record into table
def insert_record( cursor, table = 'people ( id, name, age, job)', value='( 5,\'new_member\', 99, \'IT\')' ):
    sql = f'INSERT INTO ' + table + ' VALUES ' + value
    cursor.execute(sql)
    print("Insert record.")

# Saves current state of database into dump file
def save_database():
    subprocess.run( ['pg_dump', 'testdb', '-f', 'db_dump.sql'] )
    print("Save database.")


def main():

    try:
        connection = connection_init()
        cursor = connection.cursor()
    except Error as e:
        print( e, file = stderr)
        return -1


    select_records( cursor )
    
    insert_record( cursor )
    select_records( cursor )

    delete_record( cursor )
    select_records( cursor )

    update_record( cursor )
    select_records( cursor )

    save_database()



    connection.close()

if __name__ == '__main__':
    main()