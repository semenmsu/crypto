const WebSocket = require("ws");
const pako = require("pako");
const {
    tickerSpotSubscribeAction,
    tickerSwapSubscribeAction,
    tickerFuturesSubscribeAction,
    tradesSpotSubscribeAction,
    tradesSwapSubscribeAction,
    tradesFuturesSubscribeAction,
    depth5FuturesSubscribeAction,
    depth5SpotSubscribeAction,
    depth5SwapSubscribeAction,
    tickByTickFuturesSubscribeAction
} = require("./actions");
const config = require("./config");


const ws = new WebSocket("wss://real.okex.com:8443/ws/v3?compress=true", {
    perMessageDeflate: false
});

ws.on("open", w => {
    if ("spotTicker" in config && config["spotTicker"].length > 0) {
        let tickerSpotSubscribe = tickerSpotSubscribeAction(
            ...config["spotTicker"]
        );
        ws.send(JSON.stringify(tickerSpotSubscribe));
    }

    if ("futuresTicker" in config && config["futuresTicker"].length > 0) {
        let tickerFuturesSubscribe = tickerFuturesSubscribeAction(
            ...config["futuresTicker"]
        );
        ws.send(JSON.stringify(tickerFuturesSubscribe));
    }

    if ("swapTicker" in config && config["swapTicker"].length > 0) {
        let tickerSwapSubscribe = tickerSwapSubscribeAction(
            ...config["swapTicker"]
        );
        ws.send(JSON.stringify(tickerSwapSubscribe));
    }

    if ("swapTrades" in config && config["swapTrades"].length > 0) {
        let tradesSwapSubscribe = tradesSwapSubscribeAction(
            ...config["swapTrades"]
        );
        ws.send(JSON.stringify(tradesSwapSubscribe));
    }

    if ("swapDepth5" in config && config["swapDepth5"].length > 0) {
        let depth5SwapSubscribe = depth5SwapSubscribeAction(
            ...config["swapDepth5"]
        );
        ws.send(JSON.stringify(depth5SwapSubscribe));
    }

    if ("spotTrades" in config && config["spotTrades"].length > 0) {
        let tradesSpotSubscribe = tradesSpotSubscribeAction(
            ...config["spotTrades"]
        );
        ws.send(JSON.stringify(tradesSpotSubscribe));
    }

    if ("spotDepth5" in config && config["spotDepth5"].length > 0) {
        let depth5SpotSubscribe = depth5SpotSubscribeAction(
            ...config["spotDepth5"]
        );
        ws.send(JSON.stringify(depth5SpotSubscribe));
    }

    if ("futuresTrades" in config && config["futuresTrades"].length > 0) {
        let tradesFuturesubscribe = tradesFuturesSubscribeAction(
            ...config["futuresTrades"]
        );
        ws.send(JSON.stringify(tradesFuturesubscribe));
    }

    if ("futuresDepth5" in config && config["futuresDepth5"].length > 0) {
        let depth5SFuturesSubscribe = depth5FuturesSubscribeAction(
            ...config["futuresDepth5"]
        );
        ws.send(JSON.stringify(depth5SFuturesSubscribe));
    }

    if (
        "futuresTickByTick" in config &&
        config["futuresTickByTick"].length > 0
    ) {
        let tickByTickFuturesSubscribe = tickByTickFuturesSubscribeAction(
            ...config["futuresTickByTick"]
        );
        ws.send(JSON.stringify(tickByTickFuturesSubscribe));
    }
});

ws.on("message", data => {
    if (data instanceof String) {
        console.log(data);
    } else {
        try {
            dd = pako.inflateRaw(data, { to: "string" });
            ss = `${Date.now()},${dd}`;
            console.log(ss);
        } catch (err) {
            console.log(err);
        }
    }
});

ws.on("error", err => {
    console.log(err);
});

ws.on("close", (code, reason) => {
    console.log("close ", code, reason);
});
