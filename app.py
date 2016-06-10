__author__ = 'Mono'

import time
import wrapper
import eliza

bot = wrapper.Bot()
e = eliza.eliza()

while True:
    data = bot.get_updates(offset=bot.message_offset)
    print(bot.message_offset)
    for message in data['result']:
        response = e.respond(message['message']['text'])
        bot.send_text(message['message']['chat']['id'], response)

    time.sleep(5)