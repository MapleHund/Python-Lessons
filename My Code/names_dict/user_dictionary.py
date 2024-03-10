from pathlib import Path
import json

# A thing from python crash course that I have taken entirely
# too far, just for the sake of doing so.

# To do:
# It's probably time to split this apart into classes

path = Path('users_dict.json')
# Template for user info
# This tuple gets modified by add_new_user(). Why?
# perhaps replace with a tuple just listing the keys?
# infoTemplate = ("species", "colour")
infoTemplate = ({"species":"",
                "colour":""})
userList = {}

def update_existing_user(user, userInfo):
    # Update info for an existing user
    # List all info for user in a numbered list

    # To do:
    # Make this print a numbered list and use the number
    # to select what to change
    for i, info in enumerate(userInfo[user]):
        print(info)
    while True:
        print('Select info to change:')
        infoToChange = input()
        if infoToChange in userInfo[user]:
            print(f'Enter new info for {infoToChange}.')
            userInfo[user][infoToChange] = input()
            break
        else:
            print(f"{infoToChange} not found in this user's info.")

    save_user_list(user, userInfo)
    return

def add_new_user(user, userInfo):
    # Get info for new user
    # load template for info
    
    # Pointer issue!
    # This causes any changes to userInfo to change the infoTemplate
    userInfo[user] = infoTemplate
    # Iterate over info items and enter values
    for info in userInfo[user]:
        print(f"What is this person's {info}? (\"skip\" to skip)")
        newInfo = input()
        if newInfo == "skip":
            userInfo[user][info] = ''
        else:
            userInfo[user][info] = newInfo
    # save to .json file
    save_user_list(user, userInfo)
    return


# To do:
# fix this
def print_user_info(user, userInfo):
    print(f"Info for {user}:")
    # print each key value pair in userInfo
    # this shit won't work though. Why?
    for k,v in userInfo[user].items():
        print(f'{k}: {v}')
    return

def save_user_list(user, userInfo):
    # Place userInfo into full list and save
    global userList
    userList[user] = userInfo[user]
    path.write_text(json.dumps(userList, indent = 2))
    print("User list updated.")
    return

def load_user_list():
    return json.loads(path.read_text())

def greet_user():
    # load full user list and greet by name
    global userList
    userList = load_user_list()
    userInfo = {}
    user = input("Enter a name:\n")
    if user in userList:
        userInfo[user] = userList[user]
        print_user_info(user, userInfo)
        print("Update this user? (y/n)")
        # call update user function
        if input() == 'y':
            update_existing_user(user, userInfo)
    else:
        # call new user function
        print(f"{user.title()} not found.\nAdd a new user? (y/n)")
        if str.lower(input()) == 'y':
            add_new_user(user, userInfo)

greet_user()
