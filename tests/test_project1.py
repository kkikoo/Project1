from project1 import *
import io
import unittest
import contextlib

class test_project1(unittest.TestCase):

    def test_file_not_exist(self):
        filepath = Path("no_sample_input.txt")
        with contextlib.redirect_stdout(io.StringIO()) as output:
            process_file(filepath),
            self.assertEqual(output.getattribute(), "FILE NOT FOUND\n")

    def test_file_output(self):
























if __name__ == '__main__':
    unittest.main()




