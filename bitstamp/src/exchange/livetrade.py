import json


class LiveTrade:
    def __init__(self, bts_event):
        self.microtimestamp = int(bts_event.dict["data"]["microtimestamp"])
        self.timestamp = bts_event.dict["data"]["timestamp"]
        self.amount = bts_event.dict["data"]["amount"]
        self.price = bts_event.dict["data"]["price"]
        self.amount_str = bts_event.dict["data"]["amount_str"]
        self.price_str = bts_event.dict["data"]["price_str"]
        self.id = bts_event.dict["data"]["id"]
        self.type = bts_event.dict["data"]["type"]
        self.buy_order_id = bts_event.dict["data"]["buy_order_id"]
        self.sell_order_id = bts_event.dict["data"]["sell_order_id"]

    def create_subscribe_message(symbol):
        subscribe_message = json.dumps(
            {"event": "bts:subscribe",
             "data": {
                 "channel": "live_trades_"+symbol
             }
             }
        )
        return subscribe_message

    def create_unsubscribe_message(symbol):
        unsubscribe_message = json.dumps(
            {"event": "bts:unsubscribe",
             "data": {
                 "channel": "live_trades_"+symbol
             }
             }
        )
        return unsubscribe_message

    def __repr__(self):
        ts = self.microtimestamp/1000000
        ts_str = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        ts_str = ts_str + "."+str(self.microtimestamp % 1000000)
        return (f"amount: {self.amount} price: {self.price} time: {ts_str} ")
