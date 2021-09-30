from vk_api.longpoll import VkEventType, VkLongPoll
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import vk_api
from vk_api.utils import get_random_id
import time

def create_buttons(in_message):
    keyboard = VkKeyboard(one_time=False)
    if in_message == 'кнопки':
        # Negative and positive - красная и зеленая
        # Primary and Secondary - синяя и белая

        keyboard.add_button('Green But', VkKeyboardColor.POSITIVE)
        keyboard.add_button('Red d', VkKeyboardColor.NEGATIVE)

        keyboard.add_line()
        keyboard.add_button('Blue b', VkKeyboardColor.PRIMARY)

        keyboard.add_line()
        keyboard.add_button('White b', VkKeyboardColor.SECONDARY)
    else: pass

    keyboard = keyboard.get_keyboard()
    return keyboard

def send_message(vk_session, user_id, random_id=get_random_id(), message=None, attachment=None, keyboard=None):
    vk_session.method('messages.send', {'user_id' : user_id,
                                     'random_id': random_id,
                                     'message': message,
                                     'attachment': attachment,
                                     'keyboard': keyboard})


def main():
    token = '048d3cc56b8a9e1b338805f870005fa6cac6d97d90e5ac75b73b38c43ba2c52843f4dcefe6fe72fb5b1f2'
    vk_session = vk_api.VkApi(token=token)    # Работа с процессами
    vk = vk_session.get_api()   # Для работы с апи
    longpoll = VkLongPoll(vk_session)

    #Основная часть
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:

            in_message = event.text.lower()
            keyboard = create_buttons(in_message)
            attachment = 'photo-191562630_457240699'
            print(in_message)

            if event.from_user and not event.from_me:
                #if in_message == 'кнопки':
                 #   send_message(vk_session, event.user_id, message='price')
                  #  print('1 условие')


                if in_message == 'привет':
                    send_message(vk_session, event.user_id, message='Ну привет привет')
                    print('Второе условие')



if __name__ == '__main__':
    main()