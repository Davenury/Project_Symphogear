from src.Common.Classes.Notifier import Notifier


def notifier_test():
    notifier = Notifier()
    notifier.notify("title", "msg")


notifier_test()
