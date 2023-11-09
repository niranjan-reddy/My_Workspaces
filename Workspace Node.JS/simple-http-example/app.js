const http = require('http');

const server = http.createServer((req, res) =>  {
    res.end('Hello There my Babies...');
});

server.listen(8880, () => {
    console.log('Server is RUNNING.....');
});