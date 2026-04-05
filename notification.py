import time
from plyer import notification

while True:
    notification.notify(
        title='⏰ Reminder!',
        message='Time to drink water',
        app_name='Python Notifier',
        timeout=5
    )
    # wait for 1 hour (3600 seconds)
    time.sleep(3600)
