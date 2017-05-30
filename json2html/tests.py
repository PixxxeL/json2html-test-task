# -*- coding: utf-8 -*-

import unittest

from converter import JsonToHtmlConverter


class TestJsonToHtmlConverter(unittest.TestCase):

    def test_result(self):
        data = {"p.my-class#my-id": "hello", "p.my-class1.my-class2": "example<a>asd</a>"}
        converter = JsonToHtmlConverter()
        data = converter.render(data)
        self.assertEqual(data, u'<p id="my-id" class="my-class">hello</p><p class="my-class1 my-class2">example&lt;a&gt;asd&lt;/a&gt;</p>')


if __name__ == '__main__':
    unittest.main()
