from constants import USER_SPAM_DICT
from interceptors import logger_interceptor


@logger_interceptor
def reset_all_spam_counts():
    keys = USER_SPAM_DICT
    for k in keys:
        USER_SPAM_DICT[k] = 0
        print("Removed {} data from dictionary".format(k))

