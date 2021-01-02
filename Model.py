from mysql.connector import connection
from DBConnector import DBConnect

class Model:

    def __init__(self,table,column):
        self.table = table
        self.column = column

    def insert(self,values):
        connection = DBConnect()
        query = """INSERT INTO """+self.table+" ("
        for column in self.column:
            query+=column+","
        query = query[:-1]
        query+=") VALUES ("
        for value in values:
            query+="'"+value+"',"
        query = query[:-1]
        query+=")"
        print(query)
        result = connection.executeInsert(query)
    
    def getAllData(self):
        connection = DBConnect()
        query = "SELECT * from "+self.table
        result = connection.executeSelect(query)
        # print(result)
        return result
            

    

    
        
    
    
    