import telebot
import webbrowser

bot = telebot.TeleBot('7826898830:AAFsuB8JkLGRONunmNLN1_aIM6WBApZyBNM')


@bot.message_handler(commands=['tgk', 'тгк'])
def tgk(message):
    webbrowser.open('https://t.me/aktualmemes')



@bot.message_handler(commands=['start', 'main', 'hello'])
def main(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}. Этот бот поможет проанализировать мем. Также здесь доступны функции: привет - приветствие; /tgk - наш канал; /help - юзы разработчиков,чтобы задать вопрос; id - покажет ваш айди ')


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>Help</b> <b><em>information</em></b>. По каким-либо вопросам обращаться к @dwokp / @jUs1tics24 / @hz678901', parse_mode='html')


@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id,f'Привет, {message.from_user.first_name}. Этот бот поможет проанализировать мем. ')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID:{message.from_user.id} ')

bot.polling(none_stop=True)
