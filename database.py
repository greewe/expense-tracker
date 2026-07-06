import sqlite3
conn = sqlite3.connect("expenses.db")
cursor= conn.cursor()

cursor.execute ("""CREATE TABLE IF NOT EXISTS expenses (item TEXT, amount INTEGER,category TEXT)""")
item= input("enter item")
amount=int(input("enter amount"))
category= input("enter category")


cursor.execute("INSERT INTO expenses VALUES(?,?,?)", (item,amount,category))
conn.commit()
print("saved")

cursor.execute("SELECT * FROM expenses")
ROWS= cursor.fetchall()

for row in ROWS:
    print(row)

