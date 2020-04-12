import pyowm
import telebot
import config

from telebot import types
owm = pyowm.OWM(config.token_owm, language='ru')

bot = telebot.TeleBot(config.token_bot)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы показать навыки программирования на Python своего создателя😊, пока я понимаю только текстовые сообщения\n\n"
                     "Введите название любого города на земле, чтобы узнать погоду в нем, а также получить ценные рекомендации о том, что надеть на улицу!".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html')

@bot.message_handler(commands=['help'])
def welcome(message):
    bot.send_message(message.chat.id,
                     "Введите название города, чтобы узнать в нем погоду на данный момент, вводить можно как на английском, так и на русском языке"
                     .format(message.from_user),
                     parse_mode='html')

@bot.message_handler(content_types=['text'])
def send_msg(message):
    try:
        observation = owm.weather_at_place(message.text)
        w = observation.get_weather()
        temp = w.get_temperature('celsius')['temp']
        rain = w.get_rain()
        answer = f"\U000026C5 В городе {message.text} сейчас {w.get_detailed_status()} \n"
        answer += f"\U0001F525 Температура приблизительно {round(temp)} градусов\n\nРекомендации по одежде:\n\n"


        if temp < 7:
            answer += '\U000026C4 Очень холодно - лучше укутаться в шарф и надеть теплую куртку\n'
        elif temp < 18:
             answer += '\U0001F301 Достаточно тепло - можно идти в легкой куртке или пальто\n'
        else:
            answer += '\U0001F525 Жара - можно надеть футболку и шорты!\n'
        if (rain != {}) and rain['3h'] > 0.3:
            answer += '\U00002614 Возьми зонт или ветровку - скоро будет дождь\n'
        if rain == {}:
            answer += '\U00002600 Дождя нет - зонт не пригодится\n'
        if temp < 0 and rain != {}:
             answer += '\U00002744 Идет снег - не забудь надеть шапку\n'


        bot.send_message(message.chat.id, answer)


    except pyowm.exceptions.api_response_error.NotFoundError:
           bot.send_message(message.chat.id, 'Город не найден :(\nПопробуй другой город!')


bot.polling(none_stop=True)