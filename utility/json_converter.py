# convert json into dict and vice versa
import json
import os
from pprint import pprint


def json_to_dict(json_file):
    """
    convert json file into dict
    """
    with open(json_file, 'r') as f:
        return json.load(f)



json_files_dir = os.path.abspath('../reports/22-Aug-2022-12-33-22-PM')


# Append all json files into dict
def json_to_dict_all(json_dir):
    if os.path.isdir(json_dir):
        json_files = [os.path.join(json_dir, f) for f in os.listdir(json_dir) if f.endswith('.json')]
        data_list = []
        for json_file in json_files:
            data_list.append(json_to_dict(json_file))
        return data_list


#
# print(json_to_dict('main.json'))
# print(type(json_to_dict('main.json')))

data = json_to_dict_all(json_files_dir)
# Iterate dict and print all keys and values
# for key, value in data.items():
#     print(key, value)
print(len(data))
pprint(data)

