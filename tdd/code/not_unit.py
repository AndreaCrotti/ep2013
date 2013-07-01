import MySQLdb
import report


class TestReporting(unittest.TestCase):
    def setUp(self):
        dbc = MySQLdb.connect(host='host', user='user', passwd='passwd', port='port')
        cursor = dbc.cursor(MySQLdb.cursors.DictCursor)
        # insert 10 values in the db

    def test_report(self):
        rep = report.get_report()
        self.assertEqual(len(rep), 10)
