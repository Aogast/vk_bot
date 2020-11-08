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
                if msg == 'help':
                    sender(id, '/add + время - назначить встречу\n'
                               '/del + время - удалить встречу\n'
                               '/list - показать список встерчь\n'
                               'формат времени :\n'
                               '13:47 понедельник')
                if msg in '/привет':
                    sender(id, 'хорошего дня')
                if '/add' in msg:
                    f = open("data.txt", 'r')
                    notifications = f.read().split('\n')
                    f.close()
                    if msg[5:] not in notifications:
                        f = open('data.txt', 'w')
                        notifications.append(msg[5:])
                        f.write('\n'.join(notifications))
                        f.close()
                        sender(id, 'Встреча назначена успешно.')
                    else:
                        sender(id, 'На данное время встреча уже назначена.')
                if '/del' in msg:
                    f = open("data.txt", 'r')
                    notifications = f.read().split('\n')
                    f.close()
                    if msg[5:] in notifications:
                        f = open('data.txt', 'w')
                        notifications.pop(notifications.index(msg[5:]))
                        f.write('\n'.join(notifications))
                        sender(id, 'Встреча успешно отменена.')
                        f.close()
                    else:
                        sender(id, 'На данное время не былозапланированных встреч.')
                if '/list' in msg:
                    f = open("data.txt", 'r')
                    notifications = f.read().split('\n')
                    if notifications != ['']:
                        sender(id, '\n'.join(notifications))
                    else:
                        sender(id, 'Пока что назначенных встреч нет. Спи скокойно, не беспокоясь о дедлайнах')



