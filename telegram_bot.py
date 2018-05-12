import telepot
from main import *
import sys
import time
import telepot
from telepot.loop import MessageLoop
import random

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    if(chat_id == 'chat_id'):
        if content_type == 'text':
            text = msg['text']
            if(text == 'help'):
                bot.sendMessage(chat_id, 'model#cascadeModel#n_nodes#size_iniziators#iterations\nexample: 2, 2, 500, 1, 0\nmodel: 1 = rich get richer, 2 = erdos renyi\nCascade model: 1 = 1 BF, 2 = all BF\nn_nodes: a number \nsize initiators: 1 = sqrt, 2 = log\nIteration: n iteration only for rich\nprobability:0.2/0.8\n\nint')
            else:
                if(text.count('#') == 5):
                    model, cascadeModel, n_nodes, size_iniziators, iterations, probability = text.split('#')
                    try:
                        main(int(model), int(cascadeModel), int(n_nodes), int(size_iniziators), int(iterations), float(probability))
                    except:
                        bot.sendMessage(chat_id, 'scusa, ma errore :(')
                elif(text.isdigit()):
                    i = 0
                    for iteration in text:

                        model = random.randint(1, 2)
                        cascadeModel = random.randint(1, 2)
                        n_nodes = random.choice([500, 800, 1000, 5000, 10000])
                        size_iniziators = random.randint(1, 2)
                        iterations_fraction = random.choice(['1.2', '2.3', '4.5'])
                        a, b = iterations_fraction.split('.')
                        iterations = int(n_nodes/int(b))*int(a)
                        if(model == 1):
                            probability = random.choice([0.2, 0.2, 0.3, 0.3, 0.4, 0.4, 0.5, 0.6, 0.7, 0.8])
                        elif(model == 2):
                            probability = random.choice([0.2, 0.3, 0.4, 0.5, 0.6, 0.6, 0.7, 0.7, 0.8, 0.8])

                        print(str(model) + ' | ' + str(cascadeModel) + ' | ' + str(n_nodes) + ' | ' + str(size_iniziators) + ' | ' + str(iterations) + ' | ' + str(probability) )
                        try:
                            i = i + 1
                            main(int(model), int(cascadeModel), int(n_nodes), int(size_iniziators), int(iterations), float(probability))
                        except:
                            i = i - 1
                            bot.sendMessage(chat_id, 'Error')

                    bot.sendMessage(chat_id,  str(i) + ' ' + str(text))



TOKEN = 'BOT TOKEN'

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

while 1:
    time.sleep(10)
