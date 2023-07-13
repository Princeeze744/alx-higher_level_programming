#!/usr/bin/python3
"""Module add_items_to_python_list"""
import json
from sys import argv


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

file = "add_item.json"
items = []

try:
    items = load_from_json_file(file)
except Exception as e:
    pass

# if len(argv) > 1:
    # for i, arg in enumerate(argv):
        # if i < 1:
            # continue
        # items.append(arg)
if len(argv) > 1:
    for arg in argv:
        if arg != argv[0]:
            items.append(arg)

save_to_json_file(items, file)
