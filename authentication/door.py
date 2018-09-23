import sqlite3

#methods of letting people in:

#Table Structure:
#Users Table: Names, RINs, whether we like them
#Log Table: Names, Timestamp
conn = sqlite3.connect("door.db")

def init():
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users(name TEXT, rin TEXT, good INTEGER DEFAULT 1);")
    c.execute("CREATE TABLE IF NOT EXISTS logs(rin TEXT, time TIMESTAMP);")
    conn.commit()

def verify_user(rin):
    c = conn.cursor()
    c.execute("SELECT NAME, good FROM users WHERE rin = ?", (rin,));
    c.execute("")
    return c.fetchone()

def add_user(name,rin):
    c = conn.cursor()
    c.execute("INSERT INTO users(name,RIN) VALUES (?,?)", (name,rin));
    conn.commit();

def modify_privilege(rin, priv):
    c = conn.cursor()
    c.execute("UPDATE users SET good = ? WHERE rin = ?", (priv,rin))
    conn.commit()

def delete_user(rin):
    c = conn.cursor()
    c.execute("DELETE FROM users WHERE rin = ?", (rin,))
    conn.commit()

#def get_by_rin(rin):

def list_user_privileges():
    c = conn.cursor()
    for row in c.execute("SELECT * from users"):
        print(row)
