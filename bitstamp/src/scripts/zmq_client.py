import zmq
import time
import json

symbol = b'bitstamp@btcusd!'

while True:
    try:
        context = zmq.Context()
        receiver = context.socket(zmq.SUB)
        receiver.connect("tcp://127.0.0.1:35001")
        receiver.subscribe(symbol)
        while True:
            msg = receiver.recv_multipart()
            print(msg)
            #body = json.loads(msg[1].decode("ascii"))
            # print(msg)
    except Exception as err:
        print("Exception: ", err)
    finally:
        del context
        del receiver
    print("[data stream] wait time for reconnecting")
    time.sleep(5)
