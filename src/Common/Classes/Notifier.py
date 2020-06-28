from win10toast import ToastNotifier


class Notifier:
    def __init__(self):
        self.notifier = ToastNotifier()

    def notify(self, title: str, msg: str, duration: int = 5, icon: str = None, threaded: bool = False):
        self.notifier.show_toast(title, msg, icon, duration, threaded)
