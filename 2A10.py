import random, itertools, datetime

def satolloCycle(items):
    i = len(items)
    while i > 1:
        i = i - 1
        j = random.randrange(i)  # 0 <= j <= i-1
        items[j], items[i] = items[i], items[j]
    print("\nSatollo \n{}\n".format(items))
    return items

def hand_out_cards(num_players,num_cards, cards):
    player = {}
    for i in range(1, num_players+1):
        players_lis = []
        for j in range(num_cards):
            rand = random.choice(cards)
            players_lis.append(rand)
            cards.remove(rand)
        player["Player{}".format(i)] = players_lis
    [print(key+':', ', '.join(player[key])) for key in player]

def main():
    cards = []
    deck = list(itertools.product(['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace'], ['spades', 'clubs', 'hearts', 'diamonds']))
    for val, suit in deck:
        cards.append('%s of %s' % (val, suit))
    print("Original\n", cards)
    shuffled_cards = satolloCycle(cards)
    num_players = int(input("Num of players: "))
    num_cards = int(input("Num of cards: "))
    if num_players*num_cards <= 52:
        hand_out_cards(num_players, num_cards, shuffled_cards)
    else:
        print("Players need more cards than they have in the deck!")

if __name__ =='__main__':
    main()
def printTimeStamp(name):

  print('Автор програми:' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp("Негоденко В.О. і Нескоромний Я.Д.")
