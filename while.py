from main import *
import telepot

while(True):
    #TOKEN = 'TOKEN'  # get token from command-line
    #bot = telepot.Bot(TOKEN)
    #chat_id = 'chat_id'

    model = random.randint(1, 2)
    cascadeModel = random.randint(1, 3)
    n_nodes = random.choice([500, 800, 1000])
    size_iniziators = random.randint(1, 2)
    iterations_fraction = random.choice(['1.2', '2.3', '4.5'])
    a, b = iterations_fraction.split('.')
    iterations = int(n_nodes/int(b))*int(a)
    friends = random.choice(['1.2', '2.3', '4.5', '1,3', '1,4', '3,4'])
    if(model == 1):
        probability = random.choice([0.2, 0.2, 0.3, 0.3, 0.4, 0.4, 0.5, 0.6, 0.7, 0.8])
    elif(model == 2):
        probability = random.choice([0.2, 0.3, 0.4, 0.5, 0.6, 0.6, 0.7, 0.7, 0.8, 0.8])

    print(str(model) + ' | ' + str(cascadeModel) + ' | ' + str(n_nodes) + ' | ' + str(size_iniziators) + ' | ' + str(iterations) + ' | ' + str(probability) )
    try:
        main(int(model), int(cascadeModel), int(n_nodes), int(size_iniziators), int(iterations), float(probability), float(friends))
        #bot.sendMessage(chat_id, str(model) + ' | ' + str(cascadeModel) + ' | ' + str(n_nodes) + ' | ' + str(size_iniziators) + ' | ' + str(iterations) + ' | ' + str(probability) + ' | ' + str(friends))
        print('FATTO')
    except:
        print('ERORRE')
        #bot.sendMessage(chat_id, 'scusa, ma errore :(')
