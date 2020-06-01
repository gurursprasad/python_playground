import sqlite3
import DataBase_Module.Test_Data

from DataBase_Module.Test_Data import TestData


class DataBaseFile:
    def __init__(self, filename):
        self.filename=filename

    def get_connection(self):
        con = sqlite3.connect(self.filename)
        print("Database Open")
        return con

    def create_table(self,con,table_name):
        con.execute('''CREATE TABLE IF NOT EXISTS ''' + table_name + '''(
        FNAME TEXT NOT NULL,
        LNAME TEXT NOT NULL,
        EMAIL TEXT NOT NULL,
        PWD TEXT NOT NULL)''')
        print("Table created")

    def insert_records(self,con,table_name,obj):
        data = '''INSERT INTO '''+table_name+'''( FNAME,LNAME,EMAIL,PWD) VALUES (?,?,?,?)'''
        con.execute(data, (obj.fname, obj.lname, obj.email, obj.pwd))
        con.commit()
        print("Data Inserted")

    def close_connection(self,con):
        con.close()
        print("DB closed")


if __name__ == "__main__":
    db = DataBaseFile("Swiggy_for_reg.db")
    db_obj = db.get_connection()
    db.create_table(db_obj, "swiggy_reg")
    data = TestData(fname="Guru", lname="Prasad", email="gurursprasad@gmail.com", pwd="qqqqqq")
    db.insert_records(db_obj, "swiggy_reg", data)
    db.close_connection(db_obj)