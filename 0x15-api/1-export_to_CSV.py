#!/usr/bin/python3
"""Export to CSV"""

import csv
import requests
import sys

if __name__ == '__main__':
    user = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user)
    response = requests.get(url)
    username = response.json().get('username')
    task = url + '/todos'
    response = requests.get(task)
    tasks = response.json()

    with open('{}.csv'.format(user), mode='w') as csvfile:
        for task in tasks:
            completed = task.get('completed')
            title = task.get('title')
            writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            writer.writerow([user, username, completed, title])

