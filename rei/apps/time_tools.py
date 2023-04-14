from datetime import datetime


def get_time():
    current_time = datetime.now()
    hr_24 = current_time.strftime("%H:%M")

    return hr_24


print(get_time())
