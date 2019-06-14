import random, sys, datetime
def printTimeStamp(name):

  print('Автор програми:' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp("Негоденко В.О. і Нескоромний Я.Д.")



p1 = input("Введіть імя першого ігрока: ")
p2 = input("Введіть імя другого ігрока: ")
class Kard:
    def f(self):
        lst = [x for x in range(1, self.amount + 1)]
        random.shuffle(lst)
        for i, y in enumerate(lst):
            print('{:*^25}'.format('*'))
            yield y

    def __init__(self, amount):
        self.amount = amount
        self.gen = self.f()

class Loto:
    def set_card(self):
        num = set()
        while len(num) < self.all_row * 5:
            num.add(random.randint(1, 91))
        cards = list(num)
        random.shuffle(cards)

        while len(cards) % self.all_row != 0:
            cards.append('None')
        self.all_row = int(len(cards) / self.all_row)
        cards = [cards[i: i + self.all_row] for i in range(0, len(cards), self.all_row)]

        for i in range(len(cards)):
            cards[i].sort()
        self.card_user = cards[:3]
        self.card_comp = cards[3:]

    def __init__(self, amount_card):
        row = 3
        self.all_row = row * amount_card
        self.set_card()

class Player(Loto):
    def __init__(self, name):
        self.name = name
        self.score = 0
    def get_card(self, card_player):
        print('{:-^25}'.format(self.name))
        print('{0[0]:>2} {0[1]:<10} {0[2]:<5} {0[3]} {0[4]} '.format(card_player[0]))
        print('{0[0]:>4} {0[1]:<6} {0[2]:<4} {0[3]:<4} {0[4]} '.format(card_player[1]))
        print('{0[0]} {0[1]:<5} {0[2]:<5} {0[3]:<5} {0[4]} '.format(card_player[2]))
        print('{:-^25}'.format('-'))

    def search(self, card_player, num_cask):
        for i, n in enumerate(card_player):
            if num_cask in n:
                card_player[i][n.index(num_cask)] = '0'
                self.score += 1
                if self.score == 15:
                    print('{} Победа!'.format(self.name))
                    sys.exit(1)
                return True
def main():
    game = Loto(2)
    kard = Kard(90)
    player1 = Player(p1)
    player2 = Player(p2)

    while True:
        num_cask = next(kard.gen)
        player1.get_card(game.card_user)
        player2.get_card(game.card_comp)
        if player1.search(game.card_user, num_cask):
            continue
        elif player2.search(game.card_comp, num_cask):
            continue

if __name__ == '__main__':
    main()
