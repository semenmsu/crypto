from config import *
from exchange.bitstamp import Bitstamp
import json

bts = Bitstamp(config)


def on_message(message):
    print(message)


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
