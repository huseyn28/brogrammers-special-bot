from functools import wraps

import schedule

from models.Logger import Logger
from utils import telegram_util, util
from constants import SPAM_MESSAGE


def spam_interceptor(func):

    @wraps(func)
    def wrapper(arg1,arg2):
        schedule.run_pending()
        username = telegram_util.get_username(arg1)
        count = util.spam_counter(username)
        print("{} : {}".format(username, count))
        if count > 10:
            telegram_util.send_message(arg1, SPAM_MESSAGE.format(username))
            util.spam_counter_reset(username)
        else:
            util.spam_add(username)
            result = func(arg1,arg2)
            return result

    return wrapper


def logger_interceptor(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        logger = Logger(func.__name__)
        logger.start_log()
        result = func(*args, **kwargs)
        logger.finish_log()
        return result

    return wrapper
