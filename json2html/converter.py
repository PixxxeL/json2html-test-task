# -*- coding: utf-8 -*-

import json
import logging

from conf import *


class JsonToHtmlConverter(object):

    def load(self):
        # можно использовать класс загрузчика вместо прямого вызова загрузки
        # данных. Этот класс может быть полиморфным и загружать данные из разных
        # источников в зависимости от переданного флага
        return json.load(open(DATA_FILE_PATH))

    def render(self, in_data):
        return u''.join(map(self.render_node, in_data))

    def render_node(self, node):
        return u'<h1>%(title)s</h1><p>%(body)s</p>' % node


if __name__ == '__main__':
    # можно парсить коммандную строку для настройки работы программы:
    # указывать источник данных, например и другие специфические параметры
    converter = JsonToHtmlConverter()
    print converter.render(converter.load())
