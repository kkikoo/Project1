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

    def test_2_devices_receive_messages_at_the_same_time(self):
        # If two devices receive messages at the same time
        # the device with the [smaller device ID] will process all of its received message(s)
        # before the device with the larger device ID will process any.

        # Meaning of message_list:(time, device_id, message_type, message_name, from_device,)
        message_list = [(0, 985, 2, 'Trouble', -1), (0, 211, 2, 'Hello', -1), ]
        self.assertEqual(my_sort(message_list),
                         [(0, 211, 2, 'Hello', -1), (0, 985, 2, 'Trouble', -1), ])

    def test_2_messages_arrive_at_the_same_device_at_the_same_time(self):
        # If two messages arrive at the same device at the same time, they will be processed according to the following priority:
        # 1. Cancellations are always processed before alerts. (That way, if a device receives an alert and a cancellation of that same alert simultaneously, it won't propagate the alert.)
        # 2. When two cancellations or two alerts are received simultaneously, their descriptions are compared lexicographically (i.e., using <) and the "lesser" one is processed first.
        #   So, for example, the alert Boo would be processed before the alert Hello, because 'Boo' < 'Hello' is True.
        # 3. When two cancellations or two alerts with the same description are received simultaneously, the one sent by the smaller device ID is processed first.

        # Meaning of message_list:(time, device_id, message_type, message_name, from_device,)
        # Meaning of message_type: 1 means cancel, 2 means album

        # test 1: test if Cancellations always processed before alerts
        message_list = [(0, 985, 2, 'Trouble', -1), (0, 985, 1, 'Hello', -1), ]
        self.assertEqual(my_sort(message_list),
                         [(0, 985, 1, 'Hello', -1), (0, 985, 2, 'Trouble', -1), ])
        # test 2: test when are both Cancellations or alerts
        message_list = [(0, 985, 2, 'Hello', -1), (0, 985, 2, 'Boo', -1),
                        (0, 985, 1, 'Hello', -1), (0, 985, 1, 'Boo', -1), ]
        self.assertEqual(my_sort(message_list),
                         [(0, 985, 1, 'Boo', -1), (0, 985, 1, 'Hello', -1),
                          (0, 985, 2, 'Boo', -1), (0, 985, 2, 'Hello', -1), ]
                         )
        # test 3: test when are both Cancellations or alerts with same description
        message_list = [(0, 985, 1, 'Trouble', 1),
                        (0, 985, 1, 'Trouble', -1), ]
        self.assertEqual(my_sort(message_list),
                         [(0, 985, 1, 'Trouble', -1), (0, 985, 1, 'Trouble', 1), ]
                         )

    def test_2_alerts_are_scheduled_to_be_initiated_at_the_same_time(self):
        # If two alerts are scheduled to be initiated at the same time,
        # the one being initiated by the device with the [smaller device ID] is initiated first.
        # If they're being initiated by the same device, the alert with the [lexicographically "lesser"] description (e.g., 'Boo' before 'Hello') is initiated first.
        message_list = [(0, 985, 2, 'Hello', -1), (0, 985, 2, 'Boo', -1),
                        (0, 211, 2, 'Hello', -1), (0, 211, 2, 'Boo', -1), ]
        self.assertEqual(my_sort(message_list),
                         [(0, 211, 2, 'Boo', -1), (0, 211, 2, 'Hello', -1),
                          (0, 985, 2, 'Boo', -1), (0, 985, 2, 'Hello', -1), ]
                         )

if __name__ == '__main__':
    unittest.main()




