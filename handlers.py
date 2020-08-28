import random as r
import constants as cst
from services import file_service, external_service
from utils import telegram_util

from improver import improve_confirm_bro, improve_music
from telegram import Update
from telegram.ext import CallbackContext
from interceptors import logger_interceptor, spam_interceptor


def error_handler(update: Update, context: CallbackContext):
    telegram_util.send_message(update, cst.ERROR_MESSAGE)


@spam_interceptor
@logger_interceptor
def greeting_message_handler(update: Update, context: CallbackContext):
    # todo from_user_username = __get_username(update)
    listMessages = file_service.get_message_from_file(cst.FN_GREETING_MESSAGE)
    index = r.randint(0, len(listMessages) - 1)
    telegram_util.send_message(update, listMessages[index])


@spam_interceptor
@logger_interceptor
def confirm_bro_handler(update: Update, context: CallbackContext):
    listMessages = file_service.get_message_from_file(cst.FN_CONFIRM_BRO)
    index = r.randint(0, len(listMessages) - 1)
    message = listMessages[index]
    if "@{}" in message:
        message = message.format(telegram_util.get_username(update))
    telegram_util.send_message(update, message)


@spam_interceptor
@logger_interceptor
def improve_confirm_bro_handler(update: Update, context: CallbackContext):
    if len(context.args) == 0:
        telegram_util.send_message(update, cst.IMPROVE_EXAMPLE_CONFIRM_BRO)
    else:
        improve_confirm_bro(context.args)
        from_user_username = telegram_util.get_username(update)
        telegram_util.send_message(update, cst.THANKS_FOR_IMPROVE.format(from_user_username))


@spam_interceptor
@logger_interceptor
def music_handler(update: Update, context: CallbackContext):
    listLinks = file_service.get_message_from_file(cst.FN_MUSIC)
    index = r.randint(0, len(listLinks) - 1)
    telegram_util.send_message(update, listLinks[index])


@spam_interceptor
@logger_interceptor
def improve_music_handler(update: Update, context: CallbackContext):
    if len(context.args) == 0:
        telegram_util.send_message(update, cst.IMPROVE_EXAMPLE_MUSIC)
    else:
        from_user_username = telegram_util.get_username(update)
        if improve_music(context.args):
            telegram_util.send_message(update, cst.THANKS_FOR_IMPROVE.format(from_user_username))
        else:
            telegram_util.send_message(update, cst.LINK_MUST_BE_UNIQUE.format(from_user_username))


@spam_interceptor
@logger_interceptor
def info_handler(update: Update, context: CallbackContext):
    listMessages = file_service.get_message_from_file(cst.FN_INFO)
    text:str = "\n".join(listMessages)
    telegram_util.send_message(update, text)


@spam_interceptor
@logger_interceptor
def random_meme_handler(update: Update, context: CallbackContext):
    response = external_service.get_random_meme()
    telegram_util.send_message(update, cst.MEME_MESSAGE_TEMPLATE.format(response["caption"], response["category"], response["image"]))
    
@spam_interceptor
@logger_interceptor
def tag_handler(update: Update, context: CallbackContext):
   telegram_util.send_message(update,"@hamidsultanzadeh @JustAydinn @Allahyarrr @NyzVortex @ram365 @knncortexx @Huseyn28")




