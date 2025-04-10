import time
import sys
import os

sleep_time = int(sys.argv[1])
command = " ".join(sys.argv[2:])

print(f"Running '{command}' every {sleep_time} seconds")

while(True):
    try:
        os.system(command)
    except:
        pass
    time.sleep(sleep_time)