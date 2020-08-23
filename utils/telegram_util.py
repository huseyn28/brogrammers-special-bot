from telegram import Update


def send_message(update: Update, text:str):
    update.message.reply_text(text)


def get_username(update: Update):
    return update.message.from_user["username"]
