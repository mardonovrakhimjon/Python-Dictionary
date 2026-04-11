def get_active_users(users: dict[str, dict[str, bool | str]]) -> list[str]:
    active_users = []
    for username, info in users.items():
        if info.get("active") == True:
            active_users.append(username)
    return active_users


print(active_users)