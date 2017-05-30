# -*- coding: utf-8 -*-

import json
import loggin

from conf import *


class JsonToHtmlConverter(object):

    def load(self):
        # можно использовать класс загрузчика вместо прямого вызова загрузки данных
        # этот класс может быть полиморфным и загружать данные из разных
        # источников в зависимости от переданного флага
        return json.load(open(DATA_FILE_PATH))

    def convert(self):
        data = self.render(self.load())

    def render(self, data):
        return data


if __name__ == '__main__':
    # можно парсить коммандную строку для настройки работы программы:
    # указывать источник данных, например и другие специфические параметры
    JsonToHtmlConverter().convert()
