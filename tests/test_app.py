import unittest

from demo.app import hello_world as hello


class TestApp(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello(), 'Hello World!')


if __name__ == '__main__':
    unittest.main()