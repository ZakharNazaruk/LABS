import requests
from bs4 import BeautifulSoup
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, Updater, CallbackQueryHandler
import html

BOT_TOKEN = '6778199840:AAE9lEUSZCxMROgrk5m8YR3OI2cQJ30I7NI'

def start(update, context):
    user = update.effective_user
    keyboard = get_keyboard()
    update.message.reply_markdown_v2(
        f'Привет, {user.mention_markdown_v2()}\\!',
        reply_markup=keyboard,
    )


def joke(update, context):
    keyboard = get_keyboard()
    update.message.reply_text("Выберите ключевое слово:", reply_markup=keyboard)

def get_joke(update, context):
    keyword = update.callback_query.data
    joke_text = fetch_joke(keyword)
    context.bot.send_message(update.effective_chat.id, html.unescape(joke_text), reply_markup=get_keyboard())

def fetch_joke(keyword=None):
    url = 'https://www.anekdot.ru/random/anekdot/'
    if keyword:
        url += f'?tags={keyword}'

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        joke_element = soup.find('div', class_='text')

        if joke_element:
            return joke_element.get_text(strip=True)

    return 'Не удалось получить анекдот.'

def get_keyboard():
    keyboard = [[InlineKeyboardButton("Новый анекдот", callback_data='новый_анекдот')]]

    return InlineKeyboardMarkup(keyboard)

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("joke", joke))
    dp.add_handler(CallbackQueryHandler(get_joke))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
