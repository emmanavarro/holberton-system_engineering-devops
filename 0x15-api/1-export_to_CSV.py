#!/usr/bin/python3
""" Script to export data in the CSV format """
import csv
import requests
from sys import argv


def export_to_csv(employee_id):
    """ Retrieves the ToDo list for an employee in CSV """
    url = 'https://jsonplaceholder.typicode.com/'
    user_request = '{}users/{}'.format(url, employee_id)
    employee_dict = requests.get(user_request).json()
    employee_name = employee_dict.get('username')
    tasks_dict = requests.get('{}todos?userId={}'
                              .format(url, employee_id)).json()
    file_name = '{}.csv'.format(employee_id)

    with open(file_name, mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for element in tasks_dict:
            csv_writer.writerow([employee_id, employee_name,
                                 element['completed'], element['title']])

if __name__ == "__main__":
    export_to_csv(argv[1])
