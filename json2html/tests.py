# -*- coding: utf-8 -*-

import unittest

from converter import JsonToHtmlConverter


class TestJsonToHtmlConverter(unittest.TestCase):

    def test_result(self):
        data = [{"body": "Hello, World 1!", "title": "Title #1"}, {"body": "Hello, World 2!", "title": "Title #2"}]
        converter = JsonToHtmlConverter()
        data = converter.render(data)
        self.assertEqual(data, u'<h1>Title #1</h1><p>Hello, World 1!</p><h1>Title #2</h1><p>Hello, World 2!</p>')


if __name__ == '__main__':
    unittest.main()
