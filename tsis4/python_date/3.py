import datetime

def drop_microseconds(time):
    return time.replace(microsecond = 0)

now = datetime.datetime.now()

print(drop_microseconds(now))