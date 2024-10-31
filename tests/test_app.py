import unittest

from demo.app import hello_world as hello


class TestApp(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello(), 'Hello Wor1ld!')


if __name__ == '__main__':
    unittest.main()