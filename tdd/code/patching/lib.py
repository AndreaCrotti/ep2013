from os import listdir

def filter_dirs(pth):
    for l in listdir(pth):
        if 'x' in l:
            yield l
