import json
import time
from json2xml import json2xml


def read_json():
    return json.loads(open('Schedule.json', encoding='UTF-8').read())


def write_xml(str):
    f = open('Schedule_1.xml', 'w', encoding='UTF-8')
    f.write(str)
    f.close()


additional_one_time = time.time()

for _ in range(10):
    obj = read_json()

    write_xml(json2xml.Json2xml(obj, attr_type=False).to_xml())

additional_one_time = time.time() - additional_one_time
