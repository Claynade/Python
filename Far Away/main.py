'''
This basic Python script provides reminders to take breaks
and focus on distant objects periodically.
These reminders aim to support healthy eyes
by prompting users to look at faraway objects,
reducing eye strain caused by prolonged screen time
'''

from plyer import notification
import time

title_1 = 'Look Away'
message_1 = 'look at something far away for 20 sec!'

title_2 = 'Done'
message_2 = '20 seconds completed. Thanks'

app_icon_1 = 'icon.ico'
app_icon_2 = 'icon_2.ico'
timeout = 5

while True:
    notification.notify(
        title=title_1,
        message=message_1,
        app_icon=app_icon_1,
        timeout=timeout,
    )
    time.sleep(20)
    notification.notify(
        title=title_2,
        message=message_2,
        app_icon=app_icon_2,
        timeout=timeout,
        )
    time.sleep(20 * 60)
