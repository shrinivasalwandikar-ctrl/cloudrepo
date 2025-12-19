const http = require('http');
const port = process.env.PORT || 3000;
const html = '<!doctype html><html><head><meta charset="utf-8"><title>Welcome</title></head><body><h1>Hi Shrinivas Welcome to GitHub Actions</h1></body></html>';

const server = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
  res.end(html);
});

server.listen(port, () => {
  console.log(`Server running at http://localhost:${port}/`);
});
