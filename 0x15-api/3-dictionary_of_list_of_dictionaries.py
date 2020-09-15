#!/usr/bin/python3
""" Script to export all data in the CSV format """
import json
import requests
from sys import argv


def export_all_to_json():
    """ Retrieves the ToDo list for all employees in JSON """
    url = 'https://jsonplaceholder.typicode.com/'
    employees_dict = requests.get('{}users'.format(url)).json()
    tasks_dict = requests.get('{}todos'.format(url)).json()

    all_dict = {}
    name_dict = {}

    for element in employees_dict:
        employee_id = element['id']
        all_dict[employee_id] = []
        name_dict[employee_id] = element['username']

    for element in tasks_dict:
        employee_info = {}
        employee_id = element['userId']
        employee_info['username'] = name_dict[employee_id]
        employee_info['task'] = element['title']
        employee_info['completed'] = element['completed']
        all_dict[employee_id].append(employee_info)

    file_name = 'todo_all_employees.json'

    with open(file_name, mode='w') as json_file:
        json.dump(all_dict, json_file)

if __name__ == "__main__":
    export_all_to_json()
