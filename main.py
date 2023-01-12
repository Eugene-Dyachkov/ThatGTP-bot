import telebot
import openai


# API OpenAI
openai.api_key = 'API key'

# API bot
bot = telebot.TeleBot('API bot')


# Message at startup
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Этот бот создан с помощью открытого API компании OpenAI')


@bot.message_handler(content_types=['text'])
def that(message):
    """
    Receiving and displaying a message
    """
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=message.text,
            temperature=0.5,
            max_tokens=1000,
            top_p=1.0,
            frequency_penalty=0.5,
            presence_penalty=0.0,
        )
        bot.send_message(message.chat.id, response['choices'][0]['text'])
    except ConnectionError:
        # Error messege
        bot.send_message(message.chat.id, 'Что то пошло не так)')


# RUN
bot.polling(none_stop=True)
