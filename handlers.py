import random as r
import constants as cst

from improver import improve_confirm_bro, improve_music
from telegram import Update
from telegram.ext import CallbackContext


def error_handler(update: Update, context: CallbackContext):
    __send_message(update, cst.ERROR_MESSAGE)


def greeting_message_handler(update: Update, context: CallbackContext):
    # todo from_user_username = __get_username(update)
    listMessages = __get_message_from_file(cst.FN_GREETING_MESSAGE)
    index = r.randint(0, len(listMessages) - 1)
    __send_message(update, listMessages[index])


def confirm_bro_handler(update: Update, context: CallbackContext):
    listMessages = __get_message_from_file(cst.FN_CONFIRM_BRO)
    index = r.randint(0, len(listMessages) - 1)
    __send_message(update, listMessages[index])


def improve_confirm_bro_handler(update: Update, context: CallbackContext):
    if len(context.args) == 0:
        __send_message(update, cst.IMPROVE_EXAMPLE_CONFIRM_BRO)
    else:
        improve_confirm_bro(context.args)
        from_user_username = __get_username(update)
        __send_message(update,cst.THANKS_FOR_IMPROVE.format(from_user_username))


def music_handler(update: Update, context: CallbackContext):
    listLinks = __get_message_from_file(cst.FN_MUSIC)
    index = r.randint(0, len(listLinks) - 1)
    __send_message(update, listLinks[index])


def improve_music_handler(update: Update, context: CallbackContext):
    if len(context.args) == 0:
        __send_message(update,cst.IMPROVE_EXAMPLE_MUSIC)
    else:
        improve_music(context.args)
        from_user_username = __get_username(update)
        __send_message(update, cst.THANKS_FOR_IMPROVE.format(from_user_username))


def info_handler(update: Update, context: CallbackContext):
    listMessages = __get_message_from_file(cst.FN_INFO)
    text:str = "\n".join(listMessages)
    __send_message(update,text)


# todo create new python file for file operations
def __get_message_from_file(file_name:str):
    file = open(file_name, "r")
    listMessages = file.readlines()
    file.close()
    return listMessages


def __send_message(update: Update, text:str):
    update.message.reply_text(text)


def __get_username(update: Update):
    return update.message.from_user["username"]

