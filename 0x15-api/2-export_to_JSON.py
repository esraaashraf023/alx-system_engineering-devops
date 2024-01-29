#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
exports information about his/her TODO list progress to a JSON file.
"""

import json
import requests
from sys import argv

if __name__ == '__main__':
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    user = requests.get(url + "users/{}".format(argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": argv[1]}).json()

    with open("{}.json".format(user_id), mode='w') as f:
        json.dump({
            user_id: [
                {"task": task.get('title'), "completed": task.get('completed'),
                    "username": user.get('username')}
                for task in todos
                ]
            }, f)
