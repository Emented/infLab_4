# вариант 25
# JSON -> XML
# день недели: пятница

import re
import time


# функция открытия JSON файла
def open_json(file_name):
    return open(file_name, encoding='UTF-8').read().split('\n')


# функция записи в XML файл
def write_xml(list):
    f = open('Schedule_2.xml', 'w', encoding='UTF-8')
    f.write('\n'.join(list))
    f.close()


# функция обрезки JSON массива
def js_cutter(js):
    js = js[1:len(js) - 1]
    for j in range(len(js)):
        js[j] = js[j][4:]
    return js


# функция, создающая массив из количества отступов каждой строки
def padding_checker():
    for a in range(len(start_json)):
        if start_json[a].startswith(' '):
            padding[a] = start_json[a].count('    ')


# функция нахождения тега
def find_tag(index):
    return re.search(r'"[\w-]*"', start_json[index])[0][1:-1]


# функция нахождения текста
def find_text(index):
    return re.search(r': "[\w:.,() -]*"', start_json[index])[0][3:-1]


additional_two_time = time.time()
for _ in range(10):
    start_json = open_json('Schedule.json')
    start_json = js_cutter(start_json)

    res_xml = list()  # список, который будет содержать строки нашего результирующего файла
    res_xml.append('<?xml version="1.0" encoding="utf-8"?>')  # первая строка XML файла

    massiveFlag = False  # флаг, отвечающий за вход в массив внутри JSON файла
    listOfEndings = list()  # список, который будет содержать окончания открытых тегов

    padding = [0] * len(start_json)
    padding_checker()  # создаем массив количества отступов

    for i in range(len(start_json)):  # начинаем бегать по строкам списка JSON
        tempString = ''  # переменная, в которой хранится временная строка для последующей записи
        if '"' in start_json[i]:
            tag = find_tag(i)
            # ищем теги, закрывающиеся на той же строке
            if padding[i] == padding[i + 1] or start_json[i + 1].lstrip() == '}' or start_json[i + 1].lstrip() == '},':
                text = find_text(i)
                if massiveFlag:
                    tempString += '\t' * (padding[i] - 1) + '<' + tag + '> ' + text + ' </' + tag + '>'
                else:
                    tempString += '\t' * padding[i] + '<' + tag + '> ' + text + ' </' + tag + '>'
                res_xml.append(tempString)
            # ищем теги, закрывающиеся с конца файла
            elif padding[i] != padding[i + 1] and '[' not in start_json[i]:
                text_s = '\t' * padding[i] + '<' + tag + '>'
                text_e = '\t' * padding[i] + '</' + tag + '>'
                res_xml.append(text_s)
                listOfEndings.append(text_e)
            # ищем отрытие массива
            elif '[' in start_json[i]:
                massiveFlag = True
                massiveTag = tag
                massivePadding = i
                tempString += '    ' * padding[massivePadding] + '<' + tag + '>'
                res_xml.append(tempString)

        # ищем закрытие массива
        if ']' in start_json[i]:
            massiveFlag = False
            tempString += '    ' * padding[massivePadding] + '</' + massiveTag + '>'
            res_xml.append(tempString)
        # ищем переходы в массиве
        if massiveFlag:
            if '}' in start_json[i] and '{' in start_json[i + 1]:
                tempString += '    ' * padding[massivePadding] + '</' + massiveTag + '>'
                res_xml.append(tempString)
                tempString = '    ' * padding[massivePadding] + '<' + massiveTag + '>'
                res_xml.append(tempString)
    # переворачиваем и присоединяем список окончаний тегов
    listOfEndings.reverse()
    res_xml += listOfEndings

    write_xml(res_xml)  # записываем XML в файл

additional_two_time = time.time() - additional_two_time
