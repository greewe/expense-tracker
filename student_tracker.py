import sqlite3

def student():
    conn = sqlite3.connect("tracker.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS students (subject_name TEXT,total_classes INTEGER,attended_classes INTEGER)")
    subject_name=input("Enter subject name: ")
    total_classes=int(input("Enter total classes: "))
    attended_classes=int(input("Enter attended classes: "))
    c.execute("INSERT INTO students VALUES (?,?,?)",(subject_name, total_classes,attended_classes))
    conn.commit()
    c.execute("SELECT * FROM students")
    n=c.fetchall()
    for row in n:
        print(row)

    conn.close()
student()


def percentage():
    conn = sqlite3.connect("tracker.db")
    c = conn.cursor()
    c.execute("SELECT * FROM students")
    record=c.fetchall()
    for row in record:
        subject_name=row[0]
        total_classes=row[1]
        attended_classes=row[2]
        percentage= (attended_classes/total_classes)* 100
        print(f"{subject_name}: {percentage:.1f}%")
    conn.close()

percentage()