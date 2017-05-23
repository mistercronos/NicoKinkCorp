from datetime import datetime
import time
now = datetime.now()
hello = input("")
while hello > 0:
    print("%s:%s:%s" % (now.hour, now.minute, now.second))
    time.sleep(1)