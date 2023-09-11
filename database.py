import sqlite3
conn = sqlite3.connect("computer_cards.db")

result = conn.execute("SELECT * FROM COMPUTER")
computers = result.fetchall()

for computer in computers:
    name = computer[0]
    print(name)

conn.close()

