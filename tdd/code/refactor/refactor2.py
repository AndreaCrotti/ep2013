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


def long_crappy_function():
    """Do a bit of everything
    """
    out = run_ls()
    res = []
    for line in out:
        if 'to-match' in line:
            res.append(line)

    ## updating the results to database
    dbc = MySQLdb.connect(host='host', user='user', passwd='passwd', port='port')
    cursor = dbc.cursor(MySQLdb.cursors.DictCursor)

    for r in res:
       cursor.execute('INSERT INTO table VALUES (%s)' % r)
