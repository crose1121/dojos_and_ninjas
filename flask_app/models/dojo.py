from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja
from flask import flash

DB = "dojos_and_ninjas"

class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(DB).query_db(query)
        dojos = []
        for row in results:
            dojo = Dojo(row)
            dojos.append(dojo)
        return dojos
    
    @classmethod
    def create_new_dojo(cls,data):
        query = "INSERT INTO dojos (name, location) VALUES (%(name)s,%(location)s);"
        result = connectToMySQL(DB).query_db(query,data)
        
        return result

    # @classmethod
    # def delete_dojo(cls,data):
        pass

    @classmethod
    def show_dojo_and_ninjas(cls,data):
        query = "SELECT * FROM dojos RIGHT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id=%(id)s"
        result = connectToMySQL(DB).query_db(query,data)
        dojo = cls(result[0])
        for row in result:
            if row['first_name'] != None:
                ninja_data = {
                    'id': row['id'],
                    'first_name': row['first_name'],
                    'last_name': row['last_name'],
                    'age': row['age'],
                    'created_at': row['created_at'],
                    'updated_at': row['updated_at']
                }
                new_ninja = Ninja(ninja_data)
                dojo.ninjas.append(new_ninja)
                new_ninja.dojo = dojo
        return dojo
            
