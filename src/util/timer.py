import datetime
import random
import time
import asyncio

from src.config.definitions import FREQUENCY_INTERVAL_LOW, FREQUENCY_INTERVAL_HIGH
from src.util.logger import log

# 爬buff使用长间隔，steam使用短间隔
def sleep_awhile(mode = 0):
    low = max(FREQUENCY_INTERVAL_LOW, 2)
    high = max(2, FREQUENCY_INTERVAL_HIGH)
    if mode == 1:
        interval = 1/(random.randint(5, 10))
    else:
        interval = random.randint(low, high)
    log.info("sleep {}s at {}".format(interval, datetime.datetime.now()))
    time.sleep(interval)

def sleep_awhile(mode = 0):
    low = max(FREQUENCY_INTERVAL_LOW, 2)
    high = max(2, FREQUENCY_INTERVAL_HIGH)
    if mode == 0:
        interval = random.randint(low, high)
    elif mode == 1:
        interval = 1/(random.randint(5, 10))
    log.info("sleep {}s at {}".format(interval, datetime.datetime.now()))
    await asyncio.sleep(interval)
