from project1 import *

import unittest

class demoTestOpen(unittest.TestCase):
    def __init__(self, filepath):
        super().__init__()
        self.filepath = filepath
    def __enter__(self):
        self.f = open(self.filepath, 'r+')
        return self.f
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()
        if exc_type != FileNotFoundError:
            return True
        return False
















if __name__ == '__main__':
    unittest.main()




