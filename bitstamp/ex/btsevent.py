import json


class BtsEvent:
    def __init__(self, message):
        d = json.loads(message)
        self.dict = d
        self.channel = d["channel"]
        self.event = d["event"]

    def __repr__(self):
        return(f"channel: {self.channel} event: {self.event}")
