import time
import json
from datetime import datetime
from ex.livetrade import *


class Channel:
    def __init__(self, channel_name, currency_pair):
        #CLOSED, OPEN, OPENING, CLOSING, CLOSED, ERROR
        self.state = "OPENING"
        self.currency_pair = currency_pair
        self.channel_name = channel_name
        self.name = channel_name+"_"+currency_pair

    def create_subscribe_message(self):
        if self.channel_name == "live_trades":
            return LiveTrade.create_subscribe_message(self.currency_pair)

    def create_unsubscribe_message(self):
        if self.channel_name == "live_trades":
            return LiveTrade.create_unsubscribe_message(self.currency_pair)

    def subscribe(self, ws):
        subscribe_message = self.create_subscribe_message()
        ws.send(subscribe_message)

    def unsubscribe(self, ws):
        unsubscribe_message = self.create_unsubscribe_message()
        ws.send(unsubscribe_message)
