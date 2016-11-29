import datetime

t = datetime.time()
print t

t = datetime.time(10,10,10)
print t
print t.hour
print t.minute
print t.second
print t.microsecond
print t.tzinfo

print datetime.time.min
print datetime.time.max
print datetime.time.resolution


today = datetime.date.today()
print today
print today.ctime()
print today.timetuple()
print today.year
print today.month
print today.day

print datetime.date.min
print datetime.date.max
print datetime.date.resolution

d1 = datetime.date(1992,10,10)
print d1
d2 = d1.replace(year=2016)
print d2
print d1-d2
print d2-d1
