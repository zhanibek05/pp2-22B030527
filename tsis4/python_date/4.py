import datetime

def delta_time_sec(t1, t2):
    delta = abs(time1 - time2)
    return delta.total_seconds()

time1 = datetime.datetime(2005, 5, 26, 0, 0, 0)
time2 = datetime.datetime.now()

print((delta_time_sec(time1, time2)))