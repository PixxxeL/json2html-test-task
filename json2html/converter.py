# -*- coding: utf-8 -*-

import json
import logging
import re
try:
    from html import escape  # python 3.x
except ImportError:
    from cgi import escape  # python 2.x

from conf import *


class JsonToHtmlConverter(object):

    tag_re = re.compile(r'^[^#\.]+')
    tag_id_re = re.compile(r'\#([^#\.]+)')
    tag_class_re = re.compile(r'\.([^#\.]+)')

    def __init__(self):
        self._init_log()

    def load(self):
        # можно использовать класс загрузчика вместо прямого вызова загрузки
        # данных. Этот класс может быть полиморфным и загружать данные из разных
        # источников в зависимости от переданного флага
        return json.load(open(DATA_FILE_PATH))

    def render(self, in_data):
        if isinstance(in_data, list):
            item = self.render_list(in_data)
        else:
            item = self.render_node(in_data)
        return item

    def render_list(self, list_data):
        items = u''.join(map(self.render_list_node, list_data))
        return u''.join(['<ul>', items, '</ul>'])

    def render_list_node(self, node):
        return u'<li>%s</li>' % self.render_node(node)

    def render_node(self, node):
        items = []
        for k, v in node.items():
            if isinstance(v, list):
                item = self.render_list(v)
            else:
                item = escape(v)
            tag_start, tag_end = self.parse_tag(k)
            items.append(u'<%s>%s</%s>' % (tag_start, item, tag_end,))
        return u''.join(items)

    def parse_tag(self, tag_raw):
        tag = self.tag_re.findall(tag_raw)[0]
        ids = self.tag_id_re.findall(tag_raw)
        ids = u' id="%s"' % ' '.join(ids) if ids else ''
        css = self.tag_class_re.findall(tag_raw)
        css = u' class="%s"' % ' '.join(css) if css else ''
        return tag + ids + css, tag

    def _init_log(self):
        self.log = logging.getLogger()
        self.log.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        self.log.addHandler(handler)


if __name__ == '__main__':
    # можно парсить коммандную строку для настройки работы программы:
    # указывать источник данных, например и другие специфические параметры
    converter = JsonToHtmlConverter()
    data = converter.render(converter.load())
    converter.log.info(data)
