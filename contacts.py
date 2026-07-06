import sqlite3



def main():
    conn = sqlite3.connect("contacts.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS dest (name TEXT,email TEXT, phone INTEGER)")
    name=input("Enter your name: ")
    email=input("Enter your email: ")
    phone=int(input("Enter your phone: "))
    c.execute("INSERT INTO dest VALUES (?,?,?)",(name,email,phone))
    conn.commit()
    c.execute ("SELECT * FROM dest")
    n=c.fetchall()
    for row in n:
        print(row)
    conn.close()



main()




