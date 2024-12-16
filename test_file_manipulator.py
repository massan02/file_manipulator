import os
import unittest
from file_manipulator import reverse_file_content, copy_file, duplicate_contents, replace_string

class TestFileManipulator(unittest.TestCase):

    def setUp(self):
        # テスト用のファイルを作成
        with open('test_input.txt', 'w') as f:
            f.write('test')

    def tearDown(self):
        # テスト用のファイルを削除
        os.remove('test_input.txt')
        if os.path.exists('test_output.txt'):
            os.remove('test_output.txt')

    def test_reverse_file_content(self):
        reverse_file_content('test_input.txt', 'test_output.txt')
        with open('test_output.txt', 'r') as f:
            content = f.read()
        self.assertEqual(content, 'tset')

    def test_copy_file(self):
        copy_file('test_input.txt', 'test_output.txt')
        with open('test_output.txt', 'r') as f:
            content = f.read()
        self.assertEqual(content, 'test')

    def test_duplicate_contents(self):
        duplicate_contents('test_input.txt', 3)
        with open('test_input.txt', 'r') as f:
            content = f.read()
        self.assertEqual(content, 'testtesttest')

    def test_replace_string(self):
        replace_string('test_input.txt', 'test', 'exam')
        with open('test_input.txt', 'r') as f:
            content = f.read()
        self.assertEqual(content, 'exam')

if __name__ == '__main__':
    unittest.main()
