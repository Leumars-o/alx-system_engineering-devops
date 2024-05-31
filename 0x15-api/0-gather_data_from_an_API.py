#!/usr/bin/python3
"""Gather data from an API
"""

import requests
import sys
import re

REST_API = 'https://jsonplaceholder.typicode.com/'

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            user = requests.get('{}/users/{}'.format(REST_API, id)).json()
            todos = requests.get('{}/todos'.format(REST_API)).json()
            employee = user.get('name')
            tasks = [task.get('title') for task in todos if task.get(
                'userId') == id]
            completed = [task.get('title') for task in todos if task.get(
                'userId') == id and task.get('completed') is True]
            print(
                'Employee {} is done with tasks({}/{}):'.format(
                    employee, len(completed), len(tasks)))

            if len(completed) > 0:
                print('\n'.join('\t {}'.format(task) for task in completed))
