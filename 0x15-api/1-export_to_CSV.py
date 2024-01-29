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

    # Fetch user data
    user_data = requests.get(url + "users/{}".format(employee_id)).json()

    # Fetch todo data for the specified user
    todo_data = requests.get(url + "todos", params={"userId": employee_id}).json()

    with open("{}.csv".format(employee_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for item in todo_data:
            writer.writerow([user_data['id'], user_data.get("username"),
                             str(item.get("completed")), item.get("title")])
