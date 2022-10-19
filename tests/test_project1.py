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

    def test_print(self):
        with contextlib.redirect_stdout(io.StringIO()) as output:
            print_sent(time = 100, device_id = 1, message_type = 1,
                       to_id = 2, message_name = "TestTrouble-1")
            print_received(time = 200, device_id = 2, message_type = 1,
                           from_id = 1, message_name = "TestTrouble-2")
            self.assertEqual(output.getvalue(
            ),
                "@100 #1: SENT CANCELLATION TO #2: TestTrouble-1\n@200 #2: RECEIVED CANCELLATION FROM #1: TestTrouble-2\n")























if __name__ == '__main__':
    unittest.main()




