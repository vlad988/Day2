import random, time
import datetime

money = 100
lich = 0
combin = [u"\U0001F352", u"\U0001F514", u"\U0001F34C", u"\U0001F34A", u"\u2606", u"\U0001F480"]
print("\nВперед? ('Введіть' - так; '-' - нi)")
while True:
    if money < 5:
        print("На вашому рахунку недостатньо коштiв!")
        break
    g = input()
    if g == "-":
        break
    money -= 5
    r1 = random.choice(combin)
    r2 = random.choice(combin)
    r3 = random.choice(combin)
    print("-" * 52)
    print(r1, end="")
    time.sleep(0.9)
    print(r2, end="")
    time.sleep(1.2)
    print(r3)
    time.sleep(0.6)

    if r1 == r2 == r3 == u"\U0001F514":
        money += 100
        print("+100 грн")
    elif r1 == r2 == r3 != u"\U0001F480":
        money += 25
        print("+25 грн")
    elif r1 == r2 != u"\U0001F480" or r1 == r3 != u"\U0001F480" or r2 == r3 != u"\U0001F480":
        money += 10
        print("+10 грн")
    elif r1 == r2 == r3 == u"\U0001F480":
        money -= money
        print("Ну ти даєш")
    elif r1 == r2 == u"\U0001F480" or r1 == r3 == u"\U0001F480" or r2 == r3 == u"\U0001F480":
        money -= 5
        print("Мiнус 5 грн")
    else:
        print("Нічого")
    print('Потoчний баланс: {}грн'.format(money))
    print("-"*52)
    time.sleep(0.5)

def printTimeStamp(name):

  print('Автор програми:' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp("Негоденко В.О. і Нескоромний Я.Д.")
