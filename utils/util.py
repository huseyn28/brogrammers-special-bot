from constants import USER_SPAM_DICT


def spam_add(username:str):
    if username in USER_SPAM_DICT.keys():
        count = USER_SPAM_DICT.get(username)
        USER_SPAM_DICT[username] = count+1


def spam_counter(username:str):
    count = 0
    if username in USER_SPAM_DICT.keys():
        count = USER_SPAM_DICT.get(username)
    else:
        USER_SPAM_DICT[username] = 0

    return count


def spam_counter_reset(username:str):
    if username in USER_SPAM_DICT.keys():
        USER_SPAM_DICT[username] = 0
