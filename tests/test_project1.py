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
        filepath = Path("sample_input.txt")
        device, _next_device, cost_time, all_message_name, message_list = process_file(
            filepath)
        self.assertEqual(device, [1, 2, 3, 4])
        self.assertEqual(_next_device, {1: 2, 2: 3, 3: 4, 4: 1})
        self.assertEqual(
            cost_time, {(1, 2): 750, (2, 3): 1250, (3, 4): 500, (4, 1): 1000})
        self.assertEqual(all_message_name, {'Trouble'})
        self.assertEqual(
            message_list, [(0, 1, 2, 'Trouble', -1), (2200, 1, 1, 'Trouble', -1)])

    def test_add_message(self):
        time, device_id, message_type, message_name, from_device = 100, 1, 1, "TEST_MESSAGE", 5
        self.assertEqual(add_message(time, device_id, message_type, message_name, from_device, ), (100, 1, 1, "TEST_MESSAGE", 5,))

























if __name__ == '__main__':
    unittest.main()




