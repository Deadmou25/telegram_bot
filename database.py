import sqlite3

class DataBase:
    def __init__(self):
        self.con = sqlite3.connect('student.db')
        self.cursor = self.con.cursor()
        self.data = None

    def create_table(self,table_name):
        self.cursor.execute("CREATE TABLE %s(name)"%table_name) 

    def get_all_data_from_table(self,table_name):
        self.data = self.cursor.execute("SELECT name FROM %s" % table_name)
        self.data = self.data.fetchall()

    def insert(self, table_name, name):
        self.cursor.execute("""
                            INSERT INTO %s VALUES
                            (%s) 
                            """%(table_name,name))
        self.con.commit()
    def drop_table(self, table_name):
        self.cursor.execute('DROP TABLE %s'%table_name)
