import datetime

setTime = datetime.time(8,00,00)
currentTime = datetime.time.now()
if currentTime > setTime:
    print("current time pass set time")
else:
    print("current time not yet set time")
print(currentTime)
#print(currentTime.day)
#print(currentTime.month)
#print(currentTime.year)
print(currentTime.hour)
print(currentTime.minute)
print(currentTime.second)
print(currentTime.strftime("Time: %H:%M:%S"))