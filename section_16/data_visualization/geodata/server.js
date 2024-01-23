require('dotenv').config();
console.log(process.env.GOOGLE_MAPS_API_KEY);

const express = require('express');
const app = express();
const port = process.env.PORT || 3000;

app.use(express.static('public'));

app.get('/getApiKey', (req, res) => {
  res.json({ apiKey: process.env.GOOGLE_MAPS_API_KEY });
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
