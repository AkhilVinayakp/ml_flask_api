import sqlite3
import pandas as pd
connection = sqlite3.connect('data_test.db')
cursor = connection.cursor()

data = pd.read_csv('data.csv')

# query = 'create table shirt(id INTEGER PRIMARY KEY, height int, weight int, size)'

query = "insert into  shirt(height, weight, size) values( ?, ?, ?)"
# query = 'select height from data where id=5'
# cursor.execute(query, (None, 156, 67, 'm'))
# cursor.e
z = [tuple(i) for i in (map(lambda x: x, data.iloc[i]) for i in range(0, data.index.stop))]
# cursor.executemany(query, z)
# query = "insert into shirt (height) values(?)"
# query = "select * from shirt"
# d = int(data.iloc[0].height)

'''
for row in cursor.execute(query):
    print(row)
'''
# cursor.execute(query, (d,))
# cursor.execute(query)
connection.commit()
connection.close()
