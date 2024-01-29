#!/usr/bin/python3
"""script that, using this REST API, for a given employee ID"""

import requests
import sys
import json

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 todo.py EMPLOYEE_ID')
        sys.exit(1)
    
    employee_id = sys.argv[1]

    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user data
    user = requests.get(url + "users/{}".format(employee_id)).json()

    # Fetch todo data for the specified user
    todos = requests.get(url + "todos", params={"userId": employee_id}).json()

    # Count completed tasks
    done_tasks = sum(1 for task in todos if task['completed'])

    # Print employee information and completed tasks
    print('Employee {} is done with tasks ({}/{}):'.format(
        user['name'], done_tasks, len(todos)))
    for task in todos:
        if task['completed']:
            print('\t{}'.format(task['title']))
