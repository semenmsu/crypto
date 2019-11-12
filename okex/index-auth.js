const axios = require("axios");

// Make a request for a user with a given ID
/*axios.get('/user?ID=12345')
  .then(function (response) {
    // handle success
    console.log(response);
  })
  .catch(function (error) {
    // handle error
    console.log(error);
  })
  .finally(function () {
    // always executed
  });*/

async function GetSwapInstruments() {
    let { data } = await axios.get("https://okex.com/api/swap/v3/instruments");
    let instruments = [];
    for (instrument of data) {
        const {
            instrument_id,
            underlying_index,
            quote_currency,
            coin,
            contract_val,
            listing,
            delivery,
            size_increment,
            tick_size
        } = instrument;
        instruments.push({
            symbol: instrument_id,
            min_step_price: tick_size,
            min_step_amount: size_increment
        });
    }
    return instruments;
}

async function Run() {
    swapInstruments = await GetSwapInstruments();
    console.log(swapInstruments);
}

Run();
