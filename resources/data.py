from flask_restful import Resource, reqparse
from flask import jsonify
import sqlite3


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

