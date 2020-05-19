import sqlite3
connection = sqlite3.connect('data.db')
cursor = connection.cursor()
'''
query = 'create table data(id INTEGER PRIMARY KEY, height float, weight float, size)'
'''
# query = "insert into data values(?, ?, ?, ?)"
# query = 'select * from data'
# cursor.execute(query, (None, 156, 67, 'm'))
# cursor.e
connection.commit()
connection.close()
