from pathlib import Path
import json

path = Path('users_dict.json')
infoTemplate = {"species":"",
                "colour":""}

#def update_existing_user(user):
#    userInfo = 
# meaningless text to change file
# more meaningless text
#
#
#

def add_user_info(user):
    userInfo = infoTemplate
    for info in userInfo:
        userInfo[info] = input(f"What is this person's {info}? (\"skip\" to skip)\n")
        if userInfo[info] == "skip":
            userInfo[info] = ''
        else:
            continue
    return userInfo

def add_new_user(user):
    print(f"{user.title()} not found.\nAdd a new user? (y/n)")
    if str.lower(input()) == 'y':
        userList = json.loads(path.read_text())
        userList[user] = add_user_info(user)
        path.write_text(json.dumps(userList, indent = 2))
    else:
        return None

def print_user_info(user):
    userInfo = get_user_list(user)
    for key in userInfo[user]:
        print(f'{key}: {userInfo[user][key]}')
    return None

def get_user_list(user):
    return json.loads(path.read_text())


def greet_user():
    user = input("what is your name?\n")
    if user in get_user_list(user):
        print(f"Hello {user.title()}!\n")
        print(f"User info:")
        print_user_info(user)
    else:
        add_new_user(user)
    print("Update this user? (y/n)")

greet_user()
