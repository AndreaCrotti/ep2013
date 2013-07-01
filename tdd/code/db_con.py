import MySQLdb


class TestFetcher:
    def __init__(self):
        self.tests = self.fetch_from_db()

    def __str__(self):
        return '\n'.join(self.tests)

    def fetch_from_db(self):
        dbc = MySQLdb.connect(host='host', user='user', passwd='passwd', port='port')
        cursor = dbc.cursor(MySQLdb.cursors.DictCursor)
        select = "SELECT * FROM table"
        cursor.execute(select)
        return cursor.fetchall()

    def get_last(self):
        return self.tests[-1]
