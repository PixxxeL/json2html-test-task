# -*- coding: utf-8 -*-

import unittest

from converter import JsonToHtmlConverter


class TestJsonToHtmlConverter(unittest.TestCase):

    def test_result(self):
        data = [{"h3": "Title #1", "div": "Hello, World 1!"}, {"h3": "Title #2", "div": "Hello, World 2!"}]
        converter = JsonToHtmlConverter()
        data = converter.render(data)
        self.assertEqual(data, u'<ul><li><h3>Title #1</h3><div>Hello, World 1!</div></li><li><h3>Title #2</h3><div>Hello, World 2!</div></li></ul>')


if __name__ == '__main__':
    unittest.main()
