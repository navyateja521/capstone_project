import mysql.connector
from SearchinDB.DBConnection import DatabaseConnection
from capstonexception.Mysqlexception import MYSQLError


class InsertinDB(DatabaseConnection):
    def __init__(self):
        self.conn = self.connect("localhost", "root", "Navya@123", "myhcl", 3306)

    def insert(self, files):
        self.files = files
        self.insertcur = self.connect.cursor()
        for f in self.files:
            sql = "insert into fileinfo(filename) values(%s);"
            self.insertcur.execute(sql, (f,))
            self.connect.commit()
        print("files added sucessfully")

# try:
#     f=["navya","divya"]
#     obj=InsertinDB()
#     obj.insert(f)
# except mysql.connector.Error as err:
#
#     raise MYSQLError(f'{err.msg}',err.errno)

