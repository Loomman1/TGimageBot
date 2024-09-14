from html.entities import html5

import telebot
import webbrowser
import time
from Image_parser import YandexImage
from Params import params
from telebot import types
#if __name__ == '__main__':
###OBJECTS:
parser = YandexImage()
bot=telebot.TeleBot(params.tg_key)
delay=1.5
n_pictures = 10
###END OF OBJECTS

@bot.message_handler(commands=['start'])
def startFunc(message):
    bot.send_message(message.chat.id, f"привет, {str(message.from_user.first_name)}"+str(message.from_user.last_name))

@bot.message_handler(commands=['showpics'])
def picsFunc(message):
    bot.send_message(message.chat.id, 'Картинки')

@bot.message_handler(commands=['help'])
def picsFunc(message):
    bot.send_message(message.chat.id, "<em><u>Список команд:</u></em><br>"+str(message), parse_mode='html')
    #bot.send_message(message.chat.id, message)

#САЙТ АВТОРА
@bot.message_handler(commands=['author', 'website', 'site'])
def site(message):
    webbrowser.open("https://vk.com/loomman1")

#СМОТРЕТЬ МАЛЬЧИКОВ
@bot.message_handler(commands=['set_n_pictures'])
def set_n_pics(message):
    markup = types.InlineKeyboardMarkup()
    # markup.add(types.InlineKeyboardButton("dfg"), callback='func')
    bot.send_message(message.chat.id, "", reply_markup=markup)

#СМОТРЕТЬ МАЛЬЧИКОВ
@bot.message_handler(commands=['set_interval'])
def set_interval(message):
    webbrowser.open("https://vk.com/loomman1")

#СМОТРЕТЬ ДЕВОЧЕК
@bot.message_handler(content_types=["text"])
def site(message):
    if (message.text.lower == "привет"):
        bot.send_message(message.chat.id,
                         f"привет, {str(message.from_user.first_name)}" + str(message.from_user.last_name))
    elif (message.text.lower == "п"):
        bot.send_message(message.chat.id, "Тут однажды будет погода")
    else:
        bot.send_photo(message.chat.id,"https://steamuserimages-a.akamaihd.net/ugc/2027236669268481682/9110BF376AD38B81736946AC6619700ABACFCFA1/?imw=512&amp;imh=512&amp;ima=fit&amp;impolicy=Letterbox&amp;imcolor=%23000000&amp;letterbox=true")
        links=parser.search(message)
        print(len(links))
        n=0
        for item in links:
            if (n < n_pictures):
                bot.send_photo(message.chat.id, item)
                time.sleep(delay)
                n+=1
        bot.send_message(message.chat.id, 'Вот так вот!')

@bot.message_handler()
def defaultFunc(message):
    if(message.text.lower == "привет"):
        bot.send_message(message.chat.id,
                         f"привет, {str(message.from_user.first_name)}" + str(message.from_user.last_name))
    elif (message.text.lower == "п"):
        bot.send_message(message.chat.id, "Тут однажды будет погода")
    else:
        bot.send_message(message.chat.id, 'Не знаю такой команды :')

bot.polling(none_stop=True, timeout=123)