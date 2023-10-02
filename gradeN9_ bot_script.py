import telebot

TOKEN = '6084769209:AAGm5Tvh15_Vanbx-9quGPnuTBXSjZT5214'
im = 1905083672
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text', 'photo'])

def main(message):
    global grade
    global txt
    global pht
##################
    if message.text == '/grade':
        grade = 1
##################
    if grade == 1:
        bot.send_message(message.from_user.id, 'Укажите свои данные:')
        grade = 2
##################
    elif grade == 2:
        if message.content_type == 'text':
            txt = message.text
            bot.send_message(message.from_user.id, 'Теперь отправь фото') #######
            grade = 3
        else:
            bot.send_message(message.from_user.id, 'Данные нужно записать текстом:\n1.ФИО\n2.Школа\n3.Класс')
            grade = 2
##################
    elif grade == 3:
        if message.content_type == 'photo':
            pht = message.photo[-1].file_id
            bot.send_photo(im, pht, txt)
            bot.send_message(message.from_user.id, 'Заявка отправлена на рассмотрение, ожидайте')
            grade = 0
        else:
            bot.send_message(message.from_user.id, 'Нужно одно фото')
            grade = 3
##################
    bot.register_next_step_handler(message, main)

bot.polling(none_stop=False, interval=5)