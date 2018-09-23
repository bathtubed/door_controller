import sqlite3

#methods of letting people in:

#Table Structure:
#Users Table: Names, RINs, whether we like them
#Log Table: Names, Timestamp
conn = sqlite3.connect("door.db")

def db_init():
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
    c.execute("SELECT name, rin  FROM users WHERE rin = ?",(rin,));

    possible_user = c.fetchone()
    if possible_user != None:
        if possible_user[0] == name:
            return "Error: User already added"
        else:
            return "Error: Different name added with this RIN"


    c.execute("INSERT INTO users(name,RIN) VALUES (?,?)", (name,rin));
    conn.commit();

def modify_privilege(rin, priv):
    c = conn.cursor()
    c.execute("SELECT rin  FROM users WHERE rin = ?",(rin,));

    possible_user = c.fetchone()
    if possible_user == None:
        return "Error: No such user found"

    c.execute("UPDATE users SET good = ? WHERE rin = ?", (priv,rin))
    conn.commit()

def delete_user(rin):
    c = conn.cursor()
    c.execute("SELECT rin  FROM users WHERE rin = ?",(rin,));

    possible_user = c.fetchone()
    if possible_user == None:
        return "Error: No such user found"

    c.execute("DELETE FROM users WHERE rin = ?", (rin,))
    conn.commit()

#def get_by_rin(rin):
def get_user_privilege(rin):
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE rin = ?",(rin,));

    possible_user = c.fetchone()
    if possible_user == None:
        return "Error: No such user found"
    return possible_user

def list_user_privileges():
    c = conn.cursor()
    c.execute("SELECT * from users")
    return c.fetchall()

def authenticate(rin):
    entry = verify_user(rin)
    return True if entry[2]== 1 else False;