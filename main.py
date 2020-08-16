from telegram.ext import Updater, CommandHandler, Dispatcher

import handlers as hs


def add_handlers(dp:Dispatcher):
    dp.add_error_handler(hs.error_handler)
    dp.add_handler(CommandHandler("salambrat",hs.greeting_message_handler))
    dp.add_handler(CommandHandler("eledoyulyeti",hs.confirm_bro_handler))
    dp.add_handler(CommandHandler("meneoyret",hs.improve_confirm_bro_handler))
    dp.add_handler(CommandHandler("info",hs.info_handler))


def main():
    updater = Updater('1050442412:AAGZyCp09LLFMg4tvqzuVKc1TePpVUjMlSQ',use_context=True)
    dp = updater.dispatcher
    add_handlers(dp)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
