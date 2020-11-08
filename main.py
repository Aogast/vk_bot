import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from datetime import datetime
days = {0: 'понедельник', 1: 'вторник', 2: 'среда', 3: 'четверг', 4: 'пятница',
        5: 'суббота', 6: 'воскресенье'}

vk_session = vk_api.VkApi(token='04f418deaa268a75bae69b1b8cdff956f67f9148af72e719fa11e39b363963f23c187d00fb2d372814504')
longpoll = VkLongPoll(vk_session)


def sender(id, text):
    vk_session.method('messages.send', {'chat_id': id, 'message': text, 'random_id': 0})


for event in longpoll.listen():
    current_datetime = datetime.now()
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            if event.from_chat:
                msg = event.text.lower()
                id = event.chat_id
                if msg in ['никита']:
                    sender(id, 'вы хороший человек')
                if '/add' in msg:
                    f = open("data.txt", 'r')
                    notifications = f.read().split('\n')
                    f.close()
                    f = open('data.txt', 'w')
                    notifications.append(msg[5:])
                    f.write('\n'.join(notifications))
                    f.close()
                    print(notifications)


