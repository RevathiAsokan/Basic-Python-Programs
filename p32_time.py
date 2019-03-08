""" To print time"""

import time
print(time.ctime())

def show_default(arg=time.ctime()):
    print(arg)

show_default()
