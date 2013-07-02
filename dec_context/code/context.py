from tempfile import mktemp
from os import remove

class TempFile:
    """Create a temporary file with the given content and remove it on exit
    """
    def __init__(self, content=None, temp_path=None):
        self.content = content or ""
        self.temp_file = mktemp() if temp_path is None else temp_path

    def __enter__(self):
        with open(self.temp_file, 'w') as wr:
            wr.write(self.content)

        return self.temp_file

    def __exit__(self, type, value, traceback):
        remove(self.temp_file)
