import datetime 
print(datetime.datetime.now())
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print(datetime.datetime.now().strftime("%A, %B %d, %Y"))
print(datetime.datetime.now().strftime("%I:%M %p"))

import time
print(time.time())
print(time.localtime())
print(time.ctime(time.time()))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print(time.strftime("%A, %B %d, %Y", time.localtime()))
print(time.strftime("%I:%M %p", time.localtime()))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
print(time.strftime("%A, %B %d, %Y", time.gmtime()))
print(time.strftime("%I:%M %p", time.gmtime()))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time() + 3600)))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time() - 3600)))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time() + 86400)))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time() - 86400)))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time() + 604800)))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time() - 604800)))
print(time.ctime)


import time
time.sleep(1)
for i in range(10):
    print("hello", i+1)
    time.sleep(1)