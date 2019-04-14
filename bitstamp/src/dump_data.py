from config import *
from ex.bitstamp import Bitstamp
import json
import atexit
import time
from datetime import datetime

bts = Bitstamp(config)
current_date = datetime.today().strftime('%Y%m%d')
data_dump = open(f"data/bitstamp-dump-{current_date}", 'a+')


def on_exit():
    data_dump.close()
    exit(0)


def on_message(message):
    s = datetime.utcnow().strftime('%Y%m%d %H:%M:%s')
    print(s)
    data_dump.write(str(int(time.time()*1000000))+","+str(message)+"\n")


atexit.register(on_exit)
bts.on("message", on_message)
bts.run()
