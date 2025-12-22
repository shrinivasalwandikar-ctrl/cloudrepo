const http = require('http');
const msg = 'Shrinivas ,welcome to GitHubActions..!!';

// Print to console when run
console.log(msg);

// Simple HTTP server to display the message in a browser
const server = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain; charset=utf-8' });
  res.end(msg);
});

const port = process.env.PORT || 3000;
server.listen(port, () => {
  console.log(`Server listening on http://localhost:${port}`);
});
