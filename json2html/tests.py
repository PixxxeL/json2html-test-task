# -*- coding: utf-8 -*-

import unittest

from converter import JsonToHtmlConverter


class TestJsonToHtmlConverter(unittest.TestCase):

    def test_result(self):
        data = [{"content": [{"p": "Example 1", "header": "header 1"}], "span": "Title #1"}, {"div": "div 1"}]
        converter = JsonToHtmlConverter()
        data = converter.render(data)
        self.assertEqual(data, u'<ul><li><content><ul><li><p>Example 1</p><header>header 1</header></li></ul></content><span>Title #1</span></li><li><div>div 1</div></li></ul>')


if __name__ == '__main__':
    unittest.main()
