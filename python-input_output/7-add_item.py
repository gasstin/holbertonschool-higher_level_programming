#!/usr/bin/python3
"""
    Task 7: Write a script that adds all arguments to a Python list,
    and then save them to a file:
"""
import os
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"
aux_list = []
if os.path.exists(filename):
    aux_list = load_from_json_file(filename)
for arg in sys.argv[1:]:
    aux_list.append(arg)
save_to_json_file(aux_list, filename)
