#!/usr/bin/python3
"""
script retrieves tasks for users from the JSONPlaceholder API and compiles"""
import json
import requests
from sys import argv


def fetch_user_tasks(user_id):
    user_url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    todos_url = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.status_code != 200:
        print(f"User with ID {user_id} not found")
        return None

    if todos_response.status_code != 200:
        print(f"Tasks for user with ID {user_id} not found")
        return None

    user_data = user_response.json()
    todos_data = todos_response.json()

    return {'user_data': user_data, 'todos_data': todos_data}


def generate_todo_json():
    all_users_tasks = {}
    for user_id in range(1, 11):
        user_tasks = fetch_user_tasks(user_id)
        if user_tasks:
            user_id = str(user_id)
            all_users_tasks[user_id] = []
            username = user_tasks['user_data']['username']

            for task in user_tasks['todos_data']:
                task_data = {
                    "username": username,
                    "task": task['title'],
                    "completed": task['completed']
                }
                all_users_tasks[user_id].append(task_data)

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(all_users_tasks, json_file)


if __name__ == "__main__":
    generate_todo_json()
