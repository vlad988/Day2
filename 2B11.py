import datetime
import re
text_string = 'Some index files failed To download, they have been ignored, or ones used instead.459'
low = []
high = []
num = []
for i in text_string:
    if i.islower():
        low.append(i)
    elif i.isupper():
        high.append(i)
print("Слова: {}\nКосмос: {}\nНизько: {}\nВисоко: {}\nЦифри: {}\nБукви: {}".format(len(text_string.split(' ')), (text_string.count(" ")), len(low), len(high), len(re.findall(r'\d', text_string)), len(low)+len(high)))

def printTimeStamp(name):

  print('Автор програми:' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp("Негоденко В.О. і Нескоромний Я.Д.")
