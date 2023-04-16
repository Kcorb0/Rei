from datetime import datetime


def get_current_time(format="24", timezone="local"):
    current_time = datetime.now()

    if format == "24":
        return current_time.strftime("%H:%M")
    elif format == "12":
        return current_time.strftime("%I:%M")


def timer(length):
    return None
