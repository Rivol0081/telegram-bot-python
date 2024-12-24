import os

import telebot

import logging

logging.basicConfig(level=logging.DEBUG)

# Вставьте сюда ваш токен
TOKEN = os.getenv('8058652566:AAFw3pcOVTxJyvcQRNXEErtBpmNZyUZSY18')

bot = telebot.TeleBot(TOKEN)

# Главное меню
main_menu = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.row('Баристика', 'Чек-лист уборки', 'Настрой помола', 'Калькуляция')

# Меню для Баристики
barista_menu = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
barista_menu.row('Виды', 'Обжарка', 'Сорта')
barista_menu.row('Хранение', 'Условия', 'История')
barista_menu.row('Назад')

# Словарь для хранения путей к PDF файлам
pdf_files = {
    'Виды': 'path_to_pdf/vidy.pdf',
    'Обжарка': 'path_to_pdf/obzharka.pdf',
    'Сорта': 'path_to_pdf/sorta.pdf',
    'Хранение': 'path_to_pdf/khranenie.pdf',
    'Условия': 'path_to_pdf/usloviya.pdf',
    'История': 'path_to_pdf/istoriya.pdf'
}

# Обработка команды "/start"
@bot.message_handler(commands=['start'])
def send_welcome(message):
    print(f"Команда /start получена от {message.from_user.username}")
    bot.send_message(message.chat.id, "Добро пожаловать в Tchibo бот! Выберите действие:", reply_markup=main_menu)

# Обработка текстовых сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == 'Баристика':
        bot.send_message(message.chat.id, "Выберите раздел Баристики:", reply_markup=barista_menu)
    elif message.text == 'Чек-лист уборки':
        bot.send_message(message.chat.id, "Чек-лист уборки скоро будет добавлен.")
    elif message.text == 'Настрой помола':
        bot.send_message(message.chat.id, "Функция настройки помола скоро будет доступна.")
    elif message.text == 'Калькуляция':
        bot.send_message(message.chat.id, "Калькуляция скоро будет доступна.")
    elif message.text == 'Назад':
        bot.send_message(message.chat.id, "Выберите действие:", reply_markup=main_menu)
    elif message.text in pdf_files:
        send_pdf(message)
    else:
        bot.send_message(message.chat.id, "Пожалуйста, выберите один из предложенных вариантов.")

# Отправка PDF файлов
def send_pdf(message):
    pdf_path = pdf_files.get(message.text)
    if pdf_path and os.path.exists(pdf_path):
        with open(pdf_path, 'rb') as pdf_file:
            bot.send_document(message.chat.id, pdf_file)
    else:
        bot.send_message(message.chat.id, "Файл не найден. Пожалуйста, проверьте наличие файла.")

# Запуск бота
bot.polling(none_stop=True)
