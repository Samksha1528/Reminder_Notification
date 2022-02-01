import time
from plyer import notification

if __name__ == '__main__':
    while True:
        notification.notify(
            title="Take a Break !",
            message="Go to Real World, this virtual world is NOT your reality",
            app_icon="S:\python\Reminder_Notification\Icon.ico",
            timeout=10
        )
        time.sleep(6*6)