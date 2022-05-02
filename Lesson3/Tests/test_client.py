import unittest
from Lesson3.client import *
import Lesson3.server
import time
import threading
import re
import ast

try:
    # python 3.4+ should use builtin unittest.mock not mock package
    from unittest.mock import patch
except ImportError:
    from mock import patch


class TestClient(unittest.TestCase):
    def test_create_presence(self):
        correct_message = {
            ACTION: PRESENCE,
            TIME: time.time(),
            USER: {
                ACCOUNT_NAME: ACCOUNT_NAME
            }
        }
        message_created = create_presence()
        self.assertEqual(type(message_created), type(correct_message))
        self.assertEqual(message_created[ACTION], correct_message[ACTION])
        self.assertAlmostEqual(message_created[TIME], correct_message[TIME], 3)
        self.assertEqual(message_created[USER], correct_message[USER])

    def test_create_message_with_account_name(self):
        self.assertEqual(create_presence('sana9056')[USER][ACCOUNT_NAME], 'sana9056')

    def test_create_message_exception_wrong_type(self):
        with self.assertRaises(TypeError):
            create_presence(1)

    def test_main_incorrect_port(self):
        test_args = ["client.py", "localhost", "incorrect_port"]
        with patch.object(sys, 'argv', test_args):
            with unittest.mock.patch('builtins.print') as mocked_print:
                with self.assertRaises(SystemExit):
                    main()
                self.assertEqual(mocked_print.mock_calls, [unittest.mock.call('Port should be an integer number')])

    def test_communication(self):
        th = threading.Thread(target=Lesson3.server.main)
        th.daemon = True
        th.start()
        correct_message = [
            {
                ACTION: PRESENCE,
                TIME: time.time(),
                USER: {
                    ACCOUNT_NAME: ACCOUNT_NAME
                }
            },
            {
                RESPONSE: RESPONSE
            }
        ]
        with unittest.mock.patch('builtins.print') as mocked_print:
            main()
        for idx, callstr in enumerate(mocked_print.mock_calls):
            message_created = ast.literal_eval(
                re.search(r'call\((.*?)\)', str(callstr)).group(1)
            )
            for key, value in correct_message[idx].items():
                if key != TIME:
                    self.assertEqual(message_created[key], value)
                else:
                    self.assertAlmostEqual(message_created[key], value, 1)


if __name__ == "__main__":
    unittest.main()
