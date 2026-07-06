import sqlite3


def show_all():
    conn = sqlite3.connect('practice.db')

    # create a cursor
    c = conn.cursor()

    c.execute("SELECT * FROM broski")
    #print(c.fetchall())
    n = c.fetchall()
    for item in n:
        print(item)

#print(c.fetchone())
#print(c.fetchmany(2))

#print("7000 to tel-aviv")

#commit our command


    conn.commit()
#close our connection
    conn.close()

#add a record
def add_one(first,last,email):
    conn = sqlite3.connect('practice.db')
    c=conn.cursor()
    c.execute("""INSERT INTO broski VALUES (?,?,?)""", (first,last,email))
    # commit our command
    conn.commit()
    # close our connection
    conn.close()

#deleting a record from the function

def delete_one(first,last,email):
    conn = sqlite3.connect('practice.db')
    c = conn.cursor()
    c.execute("DELETE from broski WHERE email=?",(email,))
    conn.commit()
    conn.close()
delete_one("Akbar","Akbar","Antony@soothu.com")