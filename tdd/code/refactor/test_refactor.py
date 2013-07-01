from mock import patch, Mock


fake_subprocess = Mock()
fake_subprocess.Popen = Mock()

fake_mysql = Mock()
fake_mysql.cursors = Mock()
fake_mysql.cursors.DictCursor = Mock()


class FakeProcess(object):
    def communicate(self):
        return ['to-match', '2', '3']
