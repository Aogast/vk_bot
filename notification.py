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
    sleep(35)
    current_datetime = datetime.now()
    minut = current_datetime.minute
    hour = current_datetime.hour
    if minut > 49:
        hour += 1
        minut = 60 - minut
    else:
        minut += 10
    minut = str(minut)
    minut = '0' * (2 - len(minut)) + minut
    hour = str(hour)
    hour = '0' * (2 - len(hour)) + hour
    time = hour + ':' + minut + ' ' + days[datetime.weekday(current_datetime)]
    if int(minut) > 9:
        minut = str((50 + int(minut)) % 60)
        hour = str(int(hour) + 1)
    else:
        minut = int(minut) + 50
    minut = '0' * (2 - len(minut)) + minut
    hour = '0' * (2 - len(hour)) + hour
    time2 = hour + ':' + minut + ' ' + days[datetime.weekday(current_datetime)]
    f = open("data.txt", 'r')
    notifications = f.read().split('\n')
    print(notifications)
    if time in notifications:
        sender(1, 'Собранре через 10 минут.'
                  ' Пожалуйста, не опаздывайте')
    if time2 in notifications:
        sender(1, 'Собранре через час. '
                  'Прочитай материал курса,'
                  ' если ты этого еще не сделал.')
    print(time, time2)
    f.close()

