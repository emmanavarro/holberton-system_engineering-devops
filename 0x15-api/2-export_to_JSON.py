#!/usr/bin/python3
""" Script to export data in the CSV format """
import json
import requests
from sys import argv


def export_to_json(employee_id):
    """ Retrieves the ToDo list for an employee in JSON """
    url = 'https://jsonplaceholder.typicode.com/'
    user_request = '{}users/{}'.format(url, employee_id)
    employee_dict = requests.get(user_request).json()
    employee_name = employee_dict.get('username')
    tasks_dict = requests.get('{}todos?userId={}'
                              .format(url, employee_id)).json()
    file_name = '{}.json'.format(employee_id)

    all_list = []
    for element in tasks_dict:
        employee_info = {}
        employee_info['task'] = element['title']
        employee_info['completed'] = element['completed']
        employee_info['username'] = employee_name
        all_list.append(employee_info)

    all_dict = {}
    all_dict[employee_id] = all_list

    with open(file_name, mode='w') as json_file:
        json.dump(all_dict, json_file)

if __name__ == "__main__":
    export_to_json(argv[1])
