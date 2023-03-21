from SearchinDB.DBConnection import DatabaseConnection


class SearchFiles(DatabaseConnection):
    def search(self, filename):
        print("searching in database.....")
        self.filename=filename

        sql="""select * from fileinfo where filename like '%{0}'""".format(filename)
        self.cur.execute(sql)
        data = self.cur.fetchall()
        return data
