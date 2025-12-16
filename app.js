const express = require('express');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

// Serve static files from /public and project root
app.use(express.static(path.join(__dirname, 'public')));
app.use(express.static(path.join(__dirname)));

app.get('/api/hello', (req, res) => {
  res.json({ message: 'Hello from CloudAutomation Express API' });
});

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'index.html'));
});

app.listen(PORT, () => {
  console.log(`Server running: http://localhost:${PORT}`);
});

module.exports = app;
