#!/usr/bin/python3
"""script that, using this REST API, for a given employee ID"""

import requests
import sys
import csv

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 todo.py EMPLOYEE_ID')
        sys.exit(1)
    employee_id = sys.argv[1]

    url = "https://jsonplaceholder.typicode.com/"

    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow([user_id, user_data.get("username"),
             item.get("completed"), item.get("title")]
         ) for item in todo_data]
