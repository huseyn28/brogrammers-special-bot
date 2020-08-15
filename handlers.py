import random as r
import constants as cst

from improver import improve_confirm_bro
from telegram import Update
from telegram.ext import CallbackContext


def error_handler(update: Update, context: CallbackContext):
    __send_message(update, cst.ERROR_MESSAGE)


def greeting_message_handler(update: Update, context: CallbackContext):
    # todo from_user_username = __get_username(update)
    __send_message(update, __get_message_from_file(cst.FN_GREETING_MESSAGE))


def confirm_bro_handler(update: Update, context: CallbackContext):
    __send_message(update,__get_message_from_file(cst.FN_CONFIRM_BRO))


def improve_confirm_bro_handler(update: Update, context: CallbackContext):
    improve_confirm_bro(context.args)
    from_user_username = __get_username(update)
    __send_message(update,cst.THANKS_FOR_IMPROVE.format(from_user_username))


# todo create new python file for file operations
def __get_message_from_file(file_name:str):
    file = open(file_name, "r")
    listMessages = file.readlines()
    index = r.randint(0, len(listMessages) - 1)
    file.close()
    return listMessages[index]


def __send_message(update: Update, text:str):
    update.message.reply_text(text)


def __get_username(update: Update):
    return update.message.from_user["username"]

