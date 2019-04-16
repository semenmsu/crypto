from config import *
from ex.bitstamp import Bitstamp
import json
import atexit
import time
from datetime import datetime
import os


dump_dir = "../data/"
bufsize = 1024

if "APP_ENV" in os.environ:
    if os.environ['APP_ENV'] == "dev":
        dump_dir = "/data/"

bts = Bitstamp(config)
current_date = datetime.today().strftime('%Y%m%d')
data_dump_file = open(f"{dump_dir}bitstamp-dump-{current_date}",
                      'a+', buffering=bufsize)


def on_exit():
    data_dump_file.close()
    exit(0)


def on_message(message):
    #s = datetime.utcnow().strftime('%Y%m%d %H:%M:%s')
    data_dump_file.write(str(int(time.time()*1000000))+","+str(message)+"\n")


atexit.register(on_exit)
bts.on("message", on_message)
bts.run()
