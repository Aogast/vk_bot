import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from datetime import datetime
from time import sleep
days = {0: 'понедельник', 1: 'вторник', 2: 'среда', 3: 'четверг', 4: 'пятница',
        5: 'суббота', 6: 'воскресенье'}

vk_session = vk_api.VkApi(token='77f2558775e640579c07bd2fd7f9c4db5e50fecdcd93ecfc6e4559b3930c3e5d9f0ded2674a052bdc59c2')
longpoll = VkLongPoll(vk_session)


def sender(id, text):
    vk_session.method('messages.send', {'chat_id': id, 'message': text, 'random_id': 0})

while True:
    sleep(5)
    current_datetime = datetime.now()
    minut = str(current_datetime.minute)
    minut = '0' * (2 - len(minut)) + minut
    hour = str(current_datetime.hour)
    hour = '0' * (2 - len(hour)) + hour
    time = hour + ':' + minut + ' ' + days[datetime.weekday(current_datetime)]
    f = open("data.txt", 'r')
    notifications = f.read().split('\n')
    print(notifications)
    if time in notifications:
        sender(1, 'Собранре через 10 минут. Пожалуйста, не опаздывайте')
        notifications.pop(notifications.index(time))
    f.close()

