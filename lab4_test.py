import unittest
from unittest.mock import mock_open, patch

from lab4 import get_bytes, count_bytes

LOG = (
    '1.1.1.1 - - [07/May/2017:00:08:35 +0300] "GET / HTTP/1.0" 200 100 "-" "Mozilla"\n'
    '1.1.1.1 - - [07/May/2017:00:08:52 +0300] "POST /login HTTP/1.0" 303 50 "-" "Mozilla"\n'
)
class TestNginxBytes(unittest.TestCase):
    def test_get_bytes(self):
        self.assertEqual(get_bytes(LOG.splitlines()[0]), 100)
    def test_count_bytes(self):
        with patch('builtins.open', mock_open(read_data=LOG)):
            self.assertEqual(count_bytes('log.txt'), 150)
    def test_empty_file(self):
        with patch('builtins.open', mock_open(read_data='')):
            self.assertEqual(count_bytes('log.txt'), 0)

if __name__ == '__main__':
    unittest.main()