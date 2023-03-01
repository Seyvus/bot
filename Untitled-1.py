
import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

def button(update, context):
    query = update.callback_query
    passenger = query.data
    fares = 1.25
    
    # Запись проезда пассажира
    if passenger == 'Макс':
        context.user_data['Макс'] += fares
        query.answer(text=f"Проезд Макса записан.")
    elif passenger == 'Лера':
        context.user_data['Лера'] += fares
        query.answer(text=f"Проезд Леры записан.")
    elif passenger == 'Рома':
        context.user_data['Рома'] += fares
        query.answer(text=f"Проезд Ромы записан.")

def start(update, context):
    user = update.effective_user
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Добро пожаловать, {user.first_name}! Я бот для записи проезда на работу. \nВыберите пассажира:", reply_markup=get_keyboard())

def get_keyboard():
    keyboard = [
        [InlineKeyboardButton("Макс", callback_data='Макс')],
        [InlineKeyboardButton("Лера", callback_data='Лера')],
        [InlineKeyboardButton("Рома", callback_data='Рома')]
    ]
    return InlineKeyboardMarkup(keyboard)

updater = Updater(token='TOKEN', use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))

updater.start_polling()
