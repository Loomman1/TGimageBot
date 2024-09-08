from html.entities import html5

import telebot
import webbrowser
import time


#if __name__ == '__main__':
bot=telebot.TeleBot('6868027735:AAFgb6as_VHtvUxDZ6ij6b_F9Ggo2Sa56ro')
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
@bot.message_handler(commands=['getnudeboys'])
def site(message):
    webbrowser.open("https://vk.com/loomman1")

#СМОТРЕТЬ ДЕВОЧЕК
@bot.message_handler(commands=['getnudegirls'])
def site(message):
    for i in range(3):
        bot.send_message(message.chat.id, 'Тут должны быть девочки')
        #time.sleep(3)
        #bot.send_message(message.chat.id, '<img src="https://ya.ru/images/search?from=tabbar&img_url=https%3A%2F%2Fi.pinimg.com%2Foriginals%2Fe8%2F8f%2F30%2Fe88f3028afe762960b7a2c11837b34d1.jpg&lr=21774&pos=1&rpt=simage&text=котик">', parse_mode='html')
        bot.send_photo(message.chat.id,"https://i.pinimg.com/736x/81/14/a1/8114a111992db0767789693670fe9756.jpg")

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