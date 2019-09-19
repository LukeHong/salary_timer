from time import sleep
from datetime import datetime

SALARY = None
DAILY_LIMIT = 28800

if SALARY is None:
    print("Set your salary at [SALARY]")
    exit(1)

start = datetime.now().replace(microsecond=0)
per_second = SALARY / 240 / 60 / 60

print(f"Start from {start}, money per second: {per_second:.2f}")

while True:
    time_diff = (datetime.now() - start).seconds
    
    if time_diff >= DAILY_LIMIT:
        print(f"Reach daily salary, total: {DAILY_LIMIT*per_second:.0f}")
        break

    current = time_diff * per_second
    print(f"\r${current:.2f}", end="")
    sleep(1)

