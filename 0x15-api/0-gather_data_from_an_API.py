#!/usr/bin/python3
"""script that, using this REST API, for a given employee ID"""

import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 todo.py EMPLOYEE_ID')
        sys.exit(1)
    employee_id = sys.argv[1]

    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    completed = [task.get('title') for task in todos if task.get('completed')]
    print("Employee {:s} is done with tasks({:d}/{:d}):".format(
        user.get('name'), len(completed), len(todos)
    ))

    [print("\t {:s}".format(task)) for task in completed]
