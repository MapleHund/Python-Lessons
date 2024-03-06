statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

def online_count(statuses):
    online_users=0
    for v in statuses.values():
        if v == "online":
            online_users += 1
    return online_users

online_count(statuses)
