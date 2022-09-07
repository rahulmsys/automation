# HTML Report Generator
import os
import json
from pprint import pprint


def json_to_dict(json_file):
    """
    convert json file into dict
    """
    with open(json_file, 'r') as f:
        return json.load(f)


def json_to_dict_all(json_dir):
    if os.path.isdir(json_dir):
        json_files = [os.path.join(json_dir, f) for f in os.listdir(json_dir) if f.endswith('.json')]
        data_list = []
        for json_file in json_files:
            data_list.append(json_to_dict(json_file))
        return data_list


report_path = os.path.abspath('../reports/22-Aug-2022-12-33-22-PM')
data = json_to_dict_all(report_path)
# pprint(data[0])

total_features_executed = 0
total_scenarios_executed = 0
total_scenarios_passed = 0
total_scenarios_failed = 0
total_scenarios_skipped = 0
title = 'Test Report'

