# -*- coding: utf-8 -*-

import unittest

from converter import JsonToHtmlConverter


class TestJsonToHtmlConverter(unittest.TestCase):

    def test_result(self):
        data = [{"h3": "Title #1", "div": "Hello, World 1!"}]
        converter = JsonToHtmlConverter()
        data = converter.render(data)
        self.assertEqual(data, u'<h3>Title #1</h3><div>Hello, World 1!</div>')


if __name__ == '__main__':
    unittest.main()
