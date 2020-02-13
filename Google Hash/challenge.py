import time
import random
import requests

start_time = time.time()

def telegram_bot_sendtext(bot_message):
    bot_chatID = '874299256'
    bot_token = '1000438459:AAGnGiNMz5N8tMCieKNtbK1U-4TN_Fk7tjw'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()

# output types of pizzas, in other words, number of items used from available, and what they are

def read_file(file):
    with open(file, 'r') as f:
        lines = f.readlines()
    lineOne = lines[0].split(' ')
    lineOne[-1] = lineOne[-1][:-1]
    lineTwo = lines[1].split(' ')
    lineTwo[-1] = lineTwo[-1][:-1]
    lineOne = [int(i) for i in lineOne]
    lineTwo = [int(i) for i in lineTwo]
    return (lineOne, lineTwo)

def plutus(file):
    p = read_file(file)
    maximum, types, available = p[0][0], p[0][1], p[1]
    pizza = villager(maximum, available)
    robbers = []
    for flavor in pizza:
        robbers.append(available.index(flavor))

    if robbers:
        update = """
        Total types of Pizza: *{}*\nThe types: *{}*\nNumber of slices: *{}*\nUpper limit: *{}*""".format(len(robbers), robbers, sum(pizza), maximum)
        telegram_bot_sendtext(update)
    else:
        sads = ["A failure of a program, you've written.", "Mate, it's stopped working or something...", "Phew, your script sucked.", "I love you. Just kidding, I'm your bot! You're program failed, btw.", "Lol.", "404 or something like that."]
        update = random.choice(sads)
        telegram_bot_sendtext(update)

    print("Total types of Pizza:", len(robbers))
    print("The types:", ' '.join([str(r) for r in robbers]))
    print("Number of slices:", sum(pizza))
    return maximum

def villager(max_val, pizzas):
    plate = []
    for pizza in sorted(pizzas):
        kind = set()
        index = pizzas.index(pizza)
        while sum(kind) < max_val and index < len(pizzas):
            if (sum(kind) + pizzas[index]) < max_val:
                kind.add(pizzas[index])
                index -= 1
            else:
                break
        plate.append(kind)
    for option in plate:
        if sum(option) > max_val:
            plate.remove(option)
    while len(plate) >= 2:
        if sum(plate[0]) > sum(plate[1]):
            plate.remove(plate[1])
        else:
            plate.remove(plate[0])
    return plate[0]

print(plutus("d_quite_big.in"))
telegram_bot_sendtext("Time taken: {}".format(time.time() - start_time))
print("--- %s seconds ---" % (time.time() - start_time))