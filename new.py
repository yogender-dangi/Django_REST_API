import os
import time
import datetime

fileLocation = r"D:\Projects\Django_REST_API"
year = 2023
month = 1
day = 14
hour = 19
minute = 50
second = 0

days = [14,15,16,17,18]
commit = ["first commit","map urls" ,"added new Model"]

date = datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second)


for file in os.listdir():
    # print(len(file))
    if file.endswith(".py"):
        file_path = f"{fileLocation}\{file}"
        for i in range(len(days)):
            date = datetime.datetime(year=year, month=month, day=days[i], hour=hour, minute=minute, second=second)
            modTime = time.mktime(date.timetuple())
            os.utime(file_path, (modTime, modTime))
            os.system('git add .')
            for i in range(len(commit)):
                os.system('git commit "' + '" -m"' + commit[i])







modTime = time.mktime(date.timetuple())
print(modTime)

os.utime(fileLocation, (modTime, modTime))

m_time = os.path.getmtime(fileLocation)
# convert timestamp into DateTime object
dt_m = datetime.datetime.fromtimestamp(m_time)
print('Modified on:', dt_m)
