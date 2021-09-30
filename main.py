'''
Документация к боту
*на данный момент дописывается
Набор команд:
    -help (показывает все команды)
    -привет
    -пойдешь пить пиво
    -бронирование
    -цена|прайс
    -правила
    -состояние
'''

import requests
import vk_api
import re
from vk_api import VkUpload
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import datetime


# Набор доступных комманд
help = ['help',
        '\nпривет',
        '\nпойдешь пить пиво',
        '\nбронирование',
        '\nцена|прайс',
        '\nправила',
        '\nсостояние',
        '\nсотр']
commands = {'help': 'help',
            'hi': 'привет',
            'beer': 'пойдешь пить пиво',
            'booking': 'бронирование',
            'price': 'прайс',
            'rules': 'правила',
            'state': 'состояние',
            'cooperation': 'сотр'}


def create_buttons(type_buttons):
    # Создание кнопок
    keyboard = VkKeyboard(one_time=True)
    if type_buttons == 'бронирование':
        keyboard.add_button('На ночь', VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('На день', VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('На утро', VkKeyboardColor.SECONDARY)
    keyboard = keyboard.get_keyboard()
    return keyboard

def club_is_open():
    # Открыт ли клуб
    now = datetime.datetime.now()  # Информация о нынешнем времени

    club_weekdays = (datetime.datetime(now.year, now.month, now.day, 13, 0, 0),  # Время работы клуба в будни
                     datetime.datetime(now.year, now.month, now.day + 1, 1, 0, 0))  # 13:00 - 01:00
    club_weekends = (datetime.datetime(now.year, now.month, now.day, 10, 1, 0),  # Время работы клуба в выходные
                     datetime.datetime(now.year, now.month, now.day + 1, 1, 0, 0))  # 10:00 - 01:00
    today = datetime.datetime.now()

    print(today, club_weekdays[0])
    if today.weekday() <= 4:
        if (today > club_weekdays[0] and today < club_weekdays[1]):
            return 'Клуб работает'
        else:
            return 'Клуб закрыт'
    if today.weekday() >= 5:
        if (today > club_weekends[0] and today < club_weekends[1]):
            return 'Клуб работает'
        else:
            return 'Клуб закрыт'

def main():

    # Авторизация
    token = '048d3cc56b8a9e1b338805f870005fa6cac6d97d90e5ac75b73b38c43ba2c52843f4dcefe6fe72fb5b1f2'
    vk_session = vk_api.VkApi(token=token)
    vk = vk_session.get_api()

    # Элементы управления
    longpoll = VkLongPoll(vk_session)   #Обработка сообщений и прочее
    upload = VkUpload(vk_session)   #Для загрузки фотографий
    for event in longpoll.listen():

        #Новое сообщение
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:

            in_message = event.text.lower()
            keyboard = create_buttons(in_message)
            print('in_message: {}'.format(in_message), end=' | ')

            if in_message == commands['help']:
                if event.from_user:
                    vk.messages.send(user_id=event.user_id,
                                     random_id=get_random_id(),
                                     message=help)
                print('request "help"', event.datetime, event.user_id, sep='-')

            # Приветствие
            elif in_message == commands['hi']:
                if event.from_user:
                    vk.messages.send(
                        user_id=event.user_id,
                        message='Ну привет друг',
                        random_id=get_random_id()
                    )
                    print('request hi', event.datetime, event.user_id, sep='-')

            # Просьба с пивом
            elif in_message == commands['beer']:
                if event.from_user:
                    vk.messages.send(
                        user_id=event.user_id,
                        message='Да',
                        random_id=get_random_id()
                    )
                print('request drink beer', event.datetime, event.user_id, sep='-')

            # Бронирование
            elif in_message == commands['booking']:
                if event.from_user:
                    vk_session.method('messages.send', {'user_id': event.user_id,
                                                        'random_id': get_random_id(),
                                                        'message': 'На какое время?',
                                                        'keyboard': keyboard})
                print('request "бронирование"', event.datetime, event.user_id, sep='-')

            # Цена
            elif in_message == commands['price']:
                if event.from_user:
                    vk.messages.send(
                        user_id=event.user_id,
                        random_id=get_random_id(),
                        attachment='photo-191562630_457240699',
                        message='Price list'
                    )
                print('request price list', event.datetime, event.user_id, sep='-')

            # Правила клуба
            elif in_message == commands['rules']:
                if event.from_user:
                    vk_session.method('messages.send', {'user_id': event.user_id,
                                                        'random_id': get_random_id(),
                                                        'message': 'Полный набор правил клуба можно посмотреть'
                                                                   ' тут: https://vk.com/topic-191562630_41300426.'})
                    print('request "правила"', event.datetime, event.user_id, sep='-')

            # Состояние клуба: закрыт/открыт
            elif in_message == commands['state']:
                if event.from_user:
                    vk.messages.send(user_id=event.user_id,
                                     random_id=get_random_id(),
                                     message=club_is_open())
                    print('request: "Состояние"', event.datetime, event.user_id, sep='-')

            # Сотрудничество
            elif in_message == commands['cooperation']:
                if event.from_user:
                    vk.messages.send(user_id=event.user_id,
                                    random_id=get_random_id(),
                                    message='По всем вопросам сотрудничества:'
                                            '\nМаксим: https://vk.com/aleepta'
                                            '\nАнтон: https://vk.com/xinjid7')
                    print('request: "Сотр"', event.datetime, event.user_id, sep='-')

            #Обработка не предусмотренных событий
            else:
                if event.from_user:
                    vk.messages.send(
                        user_id=event.user_id,
                        random_id=get_random_id(),
                        message='Неверная команда.'
                                '\nПопробуйсте другую команду, список доступных команд - "help"'
                    )
                    print('Command not found', event.datetime, event.user_id, sep='-')

if __name__ == '__main__':
    main()