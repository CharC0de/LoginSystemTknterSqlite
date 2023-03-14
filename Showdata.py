import tkinter as tk
import sqlite3

conn =  sqlite3.connect('schooludb.db')
cursor = conn.cursor()

root = tk.Tk()


name = tk.Label(root, text="Username")
name.grid(row=0, column=0, sticky="NSEW")

password = tk.Label(root, text="Password")
password.grid(row=0, column=1, sticky="NSEW")

userPos = tk.Label(root, text="Position")
userPos.grid(row=0, column=2, sticky="NSEW")

val=1;
sql= "SELECT username,`password`,userPosition FROM users"
cursor.execute(sql)

rows = cursor.fetchall()
 
for i, row in enumerate(rows):
    for j, col in enumerate(row):

        data = tk.Label(root, text=col, bg="white", fg="black", highlightbackground="black", highlightthickness=2)
        data.grid(row=i+1, column=j)

conn.close()

root.mainloop()