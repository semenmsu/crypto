from config import *
from exchange.bitstamp import Bitstamp, BtsMessage
import json
from mq.zeromq import pub

bts = Bitstamp(config)

def on_message(message):
    msg = BtsMessage(message)
    print(msg)
    if msg.channel == "live_trades":
        pub.send_multipart(
            [bytes(msg.full_symbol()+"!", "ascii"), bytes(msg.json(), "ascii")])


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
