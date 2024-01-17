#!/usr/bin/python3
"""
script that retrieves & exports employee's TODO list progress based on ID
"""

import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    # Fetching user data
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Fetching user's TODO list
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Organizing TODO list data in JSON format
    json_data = {str(employee_id): []}
    for task in todos_data:
        json_data[str(employee_id)].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": employee_name
        })

    # Exporting TODO list data to JSON file
    filename = f"{employee_id}.json"
    with open(filename, mode='w') as jsonfile:
        json.dump(json_data, jsonfile)

    print(f"Data exported to {filename}")
