from config import *
from ex.bitstamp import Bitstamp
import json
import atexit
import time
from datetime import datetime


bts = Bitstamp(config)

files = {}

current_date = datetime.today().strftime('%Y%m%d')


data_dump = open(f"data/bitstamp-dump-{current_date}", 'a+')


def on_exit():
    data_dump.close()
    exit(0)


atexit.register(on_exit)


def on_message(message):
    s = datetime.utcnow().strftime('%Y%m%d %H:%M:%s')
    print(s)
    data_dump.write(str(int(time.time()*1000000))+","+str(message)+"\n")
    #channel = d['channel']
    #file_name = f"data/{channel}"
    # if channel not in files:
    #    files[channel] = open(file_name, "a+")
    # files[channel].write(str(message)+"\n")


def on_open():
    pass


def on_close():
    pass


def on_error():
    pass


bts.on("message", on_message)
bts.on("open", on_open)
bts.on("close", on_close)
bts.on("error", on_error)

bts.run()
