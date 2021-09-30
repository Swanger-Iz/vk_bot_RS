import datetime

'''
a = datetime.datetime(2017, 10, 22)
print(a)
b = datetime.datetime(2017, 2, 11, 22, 11, 33)
print(b)
c = datetime.datetime(2017, 2, 11, 22, 11, 33)
print(c.year,c.second, c.microsecond, sep='\n')

print('-' * 30)

time_now = datetime.datetime.now().strftime('%H%M%S')
print(time_now)
'''

# now = datetime.datetime.now()   # Информация о нынешнем времени
#
# club_weekdays = (datetime.datetime(now.year, now.month, now.day, 13, 0, 0),    # Время работы клуба в будни
#                  datetime.datetime(now.year, now.month, now.day + 1, 1, 0, 0))     # 13:00 - 01:00
# club_weekends = (datetime.datetime(now.year, now.month, now.day, 10, 1, 0),    # Время работы клуба в выходные
#                  datetime.datetime(now.year, now.month, now.day + 1, 1, 0, 0))     # 10:00 - 01:00
# today = datetime.datetime.now()
#
# print(today, club_weekdays[0])
# if today.weekday() <= 4:
#     if (today > club_weekdays[0] and today < club_weekdays[1]):
#         print('Клуб работает')
#     else: print('Клуб закрыт')
# if today.weekday() >= 5:
#     if (today > club_weekends[0] and today < club_weekends[1]):
#         print('Клуб работает')
#     else: print('Клуб закрыт')

#for el in range(club_weekdays[0], club_weekdays[1]):

def print_help():
    help = ['help', 'привет', 'пойдешь пить пиво', 'бронирование', 'цена|прайс', 'правила', 'состояние']
    return ['\n' + el.title() for el in help]

for i in print_help():
    print(i)


