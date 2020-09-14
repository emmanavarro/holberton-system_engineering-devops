#!/usr/bin/python3
""" Using a REST API, for a given employee ID, returns information
    about his/her TODO list progress """
import requests
from sys import argv


def todo_list(employee_id):
    """ Retrieves the ToDo list for an employee """
    url = 'https://jsonplaceholder.typicode.com/'
    user_request = '{}users/{}'.format(url, employee_id)
    employee_dict = requests.get(user_request).json()
    employee_name = employee_dict.get('name')

    tasks_dict = requests.get('{}todos?userId={}'
                              .format(url, employee_id)).json()
    total_tasks = len(tasks_dict)

    done_tasks_dict = requests.get('{}todos?userId={}&&completed=true'
                                   .format(url, employee_id)).json()
    done_tasks = len(done_tasks_dict)

    print('Employee {} is done with tasks({}/{}):'
          .format(employee_name, done_tasks, total_tasks))

    for tasks_info in done_tasks_dict:
        task_title = tasks_info.get('title')
        print('\t ' + task_title)

if __name__ == "__main__":
    todo_list(argv[1])
