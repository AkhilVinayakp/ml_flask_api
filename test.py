import pandas as pd
import sqlite3
connection = sqlite3.connect('data.db')
cursor = connection.cursor()

data = pd.read_csv('data.csv')


def spd(x):
    s = []
    for i, i_val in enumerate(x):
        st = []
        # print(i, i_val, end='\n')
        for j, j_val in enumerate(i_val):
            #    print(j,j_val, end='\t')
            if j == 0 or j == 1:
                st.append(int(j_val))
            else:
                st.append(j_val)
        s.append(tuple(st))
    return s


t = [tuple(i) for i in ((map(lambda x: x, data.loc[i]) for i in range(0, data.index.stop)))]
sf = spd(t)
print(sf)
print(type(sf[0][0]), end='\n\n\n')
'''
creating the table for data insertion


'''
q = 'create table shirt(id INTEGER PRIMARY KEY, height int , weight int, size text)'
cursor.execute(q)
connection.commit()

'''
inserting the data into the table
'''
q = 'insert into shirt(height,weight,size) values(?,?,?)'
cursor.executemany(q, sf)
connection.commit()

'''
getting the data out from the database
'''
q = 'select * from shirt'
for i in cursor.execute(q):
    print(i, end='\n')


connection.close()

'''
# z = ((map(lambda x: x, data.loc[i]) for i in range(0, data.index.stop)))
t = [tuple(i) for i in ((map(lambda x: x, data.loc[i]) for i in range(0, data.index.stop)))]

h = data.iloc[0].height
print(h)
print(type(t))
print(t)

'''
