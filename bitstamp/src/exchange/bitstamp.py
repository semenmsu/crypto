import websocket
import time
import json
from datetime import datetime
from exchange.channel import *
from decimal import Decimal


websocket.enableTrace(True)

MULTIPLIER = 1000000


class BtsMessage:
    def __init__(self, message):
        d = json.loads(message)
        self.dict = d
        self.full_channel = d["channel"]
        self.channel = d["channel"]
        self.event = d["event"]
        if self.full_channel.startswith('live_trades_') and self.event == 'trade':
            self.channel = "live_trades"
            self.symbol = self.full_channel[12:]
            self.price = int(
                Decimal(self.dict['data']['price_str'])*MULTIPLIER)
            self.amount = int(
                Decimal(self.dict['data']['amount_str'])*MULTIPLIER)

    def json(self):
        if 'channel' in self.__dict__ and self.channel == "live_trades":
            return f"{{symbol: {self.full_symbol()}, bid: {self.price}, ask: {self.price}}}"

    def full_symbol(self):
        return f'bitstamp@{self.symbol}'

    def __repr__(self):

        if 'channel' in self.__dict__ and self.channel == 'live_trades':
            return(f"channel: {self.channel} event: {self.event} symbol: {self.symbol} price: {self.price} amount: {self.amount}")
        else:
            return(f"channel: {self.full_channel} event: {self.event}")


class Bitstamp:
    def __init__(self, config):
        self.config = config
        self.channels = {}
        self.ws = websocket.WebSocketApp("wss://ws.bitstamp.net",
                                         on_message=lambda ws, message: self.on_message(
                                             ws, message),
                                         on_error=lambda ws, error: self.on_error(
                                             ws, error),
                                         on_close=lambda ws: self.on_close(ws),
                                         on_open=lambda ws: self.on_open(ws))

        self.message_cb = None
        self.open_cb = None
        self.close_cb = None
        self.error_cb = None

    def on(self, event, cb):
        if event == "message":
            self.message_cb = cb
        elif event == "close":
            self.close_cb = cb
        elif event == "error":
            self.error_cb = cb
        elif event == "open":
            self.open_cb = cb

    def run(self):
        self.ws.run_forever()

    def on_message(self, ws, message):
        if self.message_cb:
            self.message_cb(message)

    def on_error(self, ws, error):
        print(error)
        if self.error_cb:
            self.error_cb(error)

    def on_close(self, ws):
        print("### closed ###")
        if self.close_cb:
            self.close_cb()

    def on_open(self, ws):
        self.channels = {}
        for currency_pair, list_channels in self.config.items():
            for channel_name in list_channels:
                channel = Channel(channel_name, currency_pair)
                self.channels[channel.name] = channel
                channel.subscribe(ws)
        if self.open_cb:
            self.open_cb
