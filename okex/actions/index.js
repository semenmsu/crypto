const tickerSpotSubscribeAction = (...symbols) => {
    args = symbols.map(symbol => `spot/ticker:${symbol}`);
    return { op: "subscribe", args };
};

const tickerFuturesSubscribeAction = (...symbols) => {
    args = symbols.map(symbol => `futures/ticker:${symbol}`);
    return { op: "subscribe", args };
};

const tickerSwapSubscribeAction = (...symbols) => {
    args = symbols.map(symbol => `swap/ticker:${symbol}`);
    return { op: "subscribe", args };
};

const tradesSpotSubscribeAction = (...symbols) => {
    args = symbols.map(symbol => `spot/trade:${symbol}`);
    return { op: "subscribe", args };
};

const tradesSwapSubscribeAction = (...symbols) => {
    args = symbols.map(symbol => `swap/trade:${symbol}`);
    return { op: "subscribe", args };
};

const tradesFuturesSubscribeAction = (...symbols) => {
    args = symbols.map(symbol => `futures/trade:${symbol}`);
    return { op: "subscribe", args };
};

const depth5SwapSubscribeAction = (...symbols) => {
    args = symbols.map(symbol => `swap/depth5:${symbol}`);
    return { op: "subscribe", args };
};

const depth5FuturesSubscribeAction = (...symbols) => {
    args = symbols.map(symbol => `futures/depth5:${symbol}`);
    return { op: "subscribe", args };
};

const depth5SpotSubscribeAction = (...symbols) => {
    args = symbols.map(symbol => `spot/depth5:${symbol}`);
    return { op: "subscribe", args };
};

//{"op": "subscribe", "args": ["futures/depth_l2_tbt:BTC-USD-191018"]}
const tickByTickFuturesSubscribeAction = (...symbols) => {
    args = symbols.map(symbol => `futures/depth_l2_tbt:${symbol}`);
    return { op: "subscribe", args };
};

module.exports = {
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
};
