import schedule
from telegram.ext import Updater, CommandHandler, Dispatcher

import handlers as hs
from interceptors import logger_interceptor
from tasks.scheduled_tasks import reset_all_spam_counts


@logger_interceptor
def add_handlers(dp:Dispatcher):
    dp.add_error_handler(hs.error_handler)
    dp.add_handler(CommandHandler("salambrat",hs.greeting_message_handler))
    dp.add_handler(CommandHandler("eledoyulyeti",hs.confirm_bro_handler))
    dp.add_handler(CommandHandler("meneoyret",hs.improve_confirm_bro_handler))
    dp.add_handler(CommandHandler("musuqu",hs.music_handler))
    dp.add_handler(CommandHandler("musuquoyret",hs.improve_music_handler))
    dp.add_handler(CommandHandler("meme",hs.random_meme_handler))
    dp.add_handler(CommandHandler("info",hs.info_handler))
    dp.add_handler(CommandHandler("tag",hs.tag_handler))

    schedule.every(10).minutes.do(reset_all_spam_counts)


@logger_interceptor
def main():
    updater = Updater('1050442412:AAGZyCp09LLFMg4tvqzuVKc1TePpVUjMlSQ',use_context=True)
    dp = updater.dispatcher
    add_handlers(dp)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
