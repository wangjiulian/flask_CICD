import pytest

from demo.app import hello_world as hello


class TestApp:
    def test_hello(self):
        assert hello() == 'Hello World!'


if __name__ == '__main__':
    pytest.main()
