import telebot

bot = telebot.TeleBot('1458008151:AAHD1J5TeEZsCsFNWYBr-t9Q-OqQMR9Y47U')
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Грустный', 'Злой', 'Раздраженный', 'Сонный', 'Печальный', 'Потерянный', 'Потрясенный', 'Уставший')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, сейчас мы выберем тебе стикер под твое настроение',
                     reply_markup=keyboard1)
    bot.send_message(message.chat.id, 'Какое у тебя настроение?',
                     reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'грустный':
        bot.send_sticker(message.chat.id, 'CAACAgQAAxkBAAKHMV_cxsoJNKkLu5r9ohmiA2iBy7LkAAJQJGYAAZXbYi9xsoN8tD7dXR4E')
    elif message.text.lower() == 'злой':
        bot.send_sticker(message.chat.id, 'CAACAgQAAxkBAAKHQF_cx6l3_OuTSsZ9m7Gfje4HaqVzAAJaJGYAAZXbYi-PtrTtTSx6uB4E')
    elif message.text.lower() == 'раздраженный':
        bot.send_sticker(message.chat.id, 'CAACAgQAAxkBAAKHLl_cxn4ujXcYc-N6TjZZwrkcDRSsAAJOJGYAAZXbYi9lz7SNMIu6Hx4E')
    elif message.text.lower() == 'сонный':
        bot.send_sticker(message.chat.id, 'CAACAgQAAxkBAAKGlV_bucBGWsXyg78lUfaAxbHK81CZAALu5mUAAZXbYi-lDrWjrZMqBx4E')
    elif message.text.lower() == 'печальный':
        bot.send_sticker(message.chat.id, 'CAACAgQAAxkBAAKGrF_b11Yut27DYIwas3mKjxdwlmF_AAL28mUAAZXbYi9SpUPJiVElWh4E')
    elif message.text.lower() == 'потерянный':
        bot.send_sticker(message.chat.id, 'CAACAgQAAxkBAAKHdl_c4j3StqyikopDOUMnx6fc0uWQAAJbOmYAAZXbYi-ZOeeBTvYy5R4E')
    elif message.text.lower() == 'потрясенный':
        bot.send_sticker(message.chat.id, 'CAACAgQAAxkBAAKHeV_c45pFYha2o-I3fqswJHtL9wafAAIEO2YAAZXbYi8ctHgXAmsdCB4E')
    elif message.text.lower() == 'уставший':
        bot.send_sticker(message.chat.id, 'CAACAgQAAxkBAAKHfF_c5E1SkXJIM4fjk24By1UTPhJyAAIvO2YAAZXbYi9kg-bfaBMuwh4E')


@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)


bot.polling()
