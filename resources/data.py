from flask_restful import Resource, reqparse
from flask import jsonify
import sqlite3
import pandas as pd

class Data(Resource):
    # Data resource  get method print out all the data that are available
    def __init__(self):
        self.connection = sqlite3.connect('data.db')
        self.cursor = self.connection.cursor()

    def get(self):
        query = 'select * from data'
        result = self.cursor.execute(query)
        li = []
        for row in result:
            li.append(row)
        return li
    # endpoint to add the data to the data base

    def post(self):
        args = reqparse.RequestParser()
        args.add_argument('height', type=float,help='required', required=True)
        args.add_argument('weight', type=float,help='required', required=True)
        args.add_argument('size', help='required', required=True)
        data = args.parse_args()
        try:
            self.cursor.execute('insert into data values(?,?,?,?)', (None, data['height'], data['weight'], data['size']))
            self.connection.commit()
        except sqlite3.Error as e:
            return {'messege': "failed to run the query", "error": e}
        return 201

    def __del__(self):
        self.connection.close()


class DataEntry(Resource):
    def __init__(self):
        self.connection = sqlite3.connect('data.db')
        self.cursor = self.connection.cursor()

    # bulk amount data transfer from the csv file to the database
    def post(self):
        data = pd.DataFrame(pd.read_csv('data.csv'))
        sql = 'insert into data values(?,?,?,?)'
       # self.cursor.executemany(sql,)



