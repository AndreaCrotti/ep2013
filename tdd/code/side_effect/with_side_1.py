from os import path
# read something from a file
FNAME = 'input.txt'


def read_from_disk():
    """Read a file from disk and return a list with its content
    """
    assert path.isfile(FNAME), "File %s does not exist" % FNAME
    res = []
    for line in open(FNAME):
        res.append(line.strip())

    return res
