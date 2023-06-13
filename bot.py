from dotenv import load_dotenv
import os
import logging

import scrapper
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
    level=logging.INFO)
logger = logging.getLogger(__name__)


def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('''Kitapyurdu Botuna Hoşgeldiniz!\nAşağıdaki Listeden görmek istediğiniz kategorileri seçebilirsiniz.
    /CokSatanlar
    /YeniCikanlar
    /HaftaninYayinevi''')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update, context):
    """Echo the user message."""
    # update.message.text
    update.message.reply_text('''Kitapyurdu Botuna Hoşgeldiniz!\nAşağıdaki Listeden görmek istediğiniz kategorileri seçebilirsiniz.
    /CokSatanlar
    /YeniCikanlar
    /HaftaninYayinevi''')


def handle_message(update, context):
    # Gelen mesajın chat ID'sini alın
    chat_id = update.message.chat_id
    
    # Gelen mesajı kontrol edin
    message_text = update.message.text
    
    # Belirli bir mesaja karşılık verecek bir kontrol yapın
    if message_text == "/CokSatanlar":
        results = scrapper.bestSellers()
        print(results)
        # results = results.encode('utf-8')
        context.bot.send_message(chat_id=chat_id, text=results)
    elif message_text == "/YeniCikanlar":
        results = scrapper.newReleases()
        context.bot.send_message(chat_id=chat_id, text=results)
    elif message_text == "/HaftaninYayinevi":
        results = scrapper.publisherOfTheWeek()
        context.bot.send_message(chat_id=chat_id, text=results)
    else:
        context.bot.send_message(chat_id=chat_id, text="Anlamadım, tekrar eder misiniz?")


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(BOT_TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
