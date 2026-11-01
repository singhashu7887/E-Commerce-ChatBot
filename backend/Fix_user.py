import sqlite3

db = sqlite3.connect(r'C:\Users\Ashutosh_Raghuvanshi\Downloads\ecommerce_chat_assistant-main\ecommerce_chat_assistant-main\data\assistant.db')
db.execute("UPDATE users SET name = 'Ashutosh Singh', email = 'ashutosh@example.com' WHERE user_id = 'U001'")
db.commit()
rows = db.execute('SELECT user_id, name, email FROM users').fetchall()
for r in rows:
    print(r)
db.close()