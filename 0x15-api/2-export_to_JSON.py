#!/usr/bin/python3
"""Gather data from an API and Export to JSON format
"""

import json
import re
import requests
import sys

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
            
            with open('{}.json'.format(id), 'w') as file:
                for task in todos:
                    if task.get('userId') == id:
                        json.dump({f"{id}": [{"task": task.get('title'), "completed": \
                            task.get('completed'), "username": user.get('username')}]}, file)
                        

