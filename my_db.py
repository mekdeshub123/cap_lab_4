import sqlite3
#Create a connection to db file
conn = sqlite3.connect('my_first_db.sqlite')
cur = conn.cursor()

#create a table and columns
conn.execute('create table if not exists j_records (Name text, Country txt, Catches integer)')


#Add data into the table(prompt users)
def add_data(name, country, catches):
    name = input('Enter name of juggler: ')
    country = input('Enter the country: ')
    catches = int(input('Enter number of catches: '))

    #Executing insert SQLite query
    conn.execute('insert into j_records values (?, ?, ?)', (name, country, catches))
    conn.commit() #Tell the database to save changes

#fitching record by name
def get_record(name):
    name = input("enter name to search: ")

    #executintin sqlite Select  by name query
    get_record_sql = 'SELECT * FROM j_records WHERE name = ?'
    cur.execute(get_record_sql,(name,))
    rows = cur.fetchall()
    #record_data = rows.fetchone()
    print(rows)


#updating fitch by mame
def update_catch(name, catches):
    name = input("Enter the name of the juggler: ")
    catches = int(input("Enter the number of catches"))
    update_sql = 'UPDATE j_records SET catches = ? WHERE name = ?'
    cur.execute(update_sql, (catches, name ))
    conn.commit()#tell the db to update the data
    print(cur.rowcount)#displayed the number of rows that is updated


#dleting records
def delete_record(name):
    name = input("enter name: ")#prompts the user to input name that need to be deleted
    
    cur.execute('DELETE FROM J_records WHERE name = ?', (name, ))
    #cur.execute(delete_sql)
    conn.commit()
    print(f'{cur.rowcount} record/s deleted')#displays the number of deleted items

#main    
if __name__ == "__main__":
    #users menu
    print('\n')
    print('A = add record')
    print('D = delete record')
    print('G = get record')
    print('U = update record')
    print('\n')

    try:#block error generated
        option = input("Enter your choice: ")#user's selections input
        selection = option.upper()#neutrlized case sensetivity

        if selection == 'A': #checks users selection
            add_data(name = "ta", country = "aa", catches = 1 )#adds data
        elif selection == 'D': #checks users selection
            delete_record("Name")#delete data
        elif selection == 'U': #checks users selection
            update_catch("name", catches = 1)#update data
        elif selection == 'G': #checks users selection
            get_record(name = 'mmm')#fitch data
        else:
            print("Wrong selection")
    except:
        print("Error")
    finally:
        conn.close()#closes the database




