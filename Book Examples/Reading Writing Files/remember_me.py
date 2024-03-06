from pathlib import Path
import json

path = Path('username.json')

def get_stored_username(path):
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None


def get_new_username(path):
    '''promt for a new username'''
    username = input("what is your name?\n")
    contents = json.dumps(username)
    path.write_text(contents)
    return username


def greet_user():
    '''greet the user by name'''
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}.")

greet_user()
