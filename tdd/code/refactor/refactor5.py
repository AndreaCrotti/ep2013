"""
Series of steps to pass from a messy function to many nice ones
"""

import subprocess

import MySQLdb


def run_ls():
    ## launching a shell command
    ls_cmd = 'ls'
    p = subprocess.Popen(ls_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    ## filtering the output of a shell command
    out, err = p.communicate()

    return out


def filter_output(out):
    res = []
    for line in out:
        if 'to-match' in line:
            res.append(line)

    return res


def update_to_database(res):
    ## updating the results to database
    dbc = MySQLdb.connect(host='host', user='user', passwd='passwd', port='port')
    cursor = dbc.cursor(MySQLdb.cursors.DictCursor)

    for r in res:
       cursor.execute('INSERT INTO table VALUES (%s)' % r)


def main():
    """Update filtered result from a shell command to the database
    """
    out = run_ls()
    res = filter_output(out)
    update_to_database(res)


def test_filter_output():
    lines = ['x1: to-match', 'x2', 'x3: to-match..']
    desired = ['x1: to-match', 'x3: to-match..']
    assert filter_output(lines) == desired


if __name__ == '__main__':
    test_filter_output()
