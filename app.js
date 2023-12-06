const express = require('express');
const axios = require('axios');

const app = express();
const port = 2080;

function getBitCoinPrice() {
  const key = 'https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT';
  return axios.get(key).then(response => response.data.price);
}

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

app.get('/get_btc_price', async (req, res) => {
  try {
    const btcPrice = await getBitCoinPrice();
    res.json({ btc_price: btcPrice });
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});
