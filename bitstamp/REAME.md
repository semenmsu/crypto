### CurrencyPairs

btcusd, btceur, eurusd, xrpusd, xrpeur, xrpbtc, ltcusd, ltceur, ltcbtc, ethusd, etheur, ethbtc, bchusd, bcheur, bchbtc

### Channels

-   live_trades
-   live_orders
-   order_book
-   detail_order_book
-   diff_order_book

### Message Types
- bts:error
- bts:subscription_succeeded

### Config Example

```python
config = {
    "btcusd": ["live_trades", "order_book"]
    "btceur": ["live_trades", "live_orders"]
    "eurusd": ["live_trades"]
}
```

### Errors
```json
//can't find error channel from this message
{"event":"bts:error","channel":"","data":{"code":null,"message":"Incorrect JSON format."}}

```

### Docs

-   websocket 2 - https://it.bitstamp.net/websocket/v2/
