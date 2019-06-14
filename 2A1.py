import datetime

a = list(input("Введіть: "))
if len(a) < 6:
    print("Помилка")
else:
    for i in range(3):
        del a[a.index(max(a))]
        del a[a.index(min(a))]
    print("L =", a)


def printTimeStamp(name):

  print('Автор програми:' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp("Негоденко В.О. і Нескоромний Я.Д.")


