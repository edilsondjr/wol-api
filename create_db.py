import sqlite3

conn = sqlite3.connect('data.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE hosts (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name varchar(50) NOT NULL,
    ip varchar(20) NOT NULL,
    mac varchar(20) NOT NULL
);
""")

cursor.execute("""
INSERT INTO hosts 
    (name, ip, mac)
values (
    'Default',
    '192.168.0.1',
    'AA-BB-CC-DD-EE-FF' 
);

""")

conn.commit()

conn.close()