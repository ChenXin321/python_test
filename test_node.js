var http = require('http');

http.createServer(function (request, response) {

    // 发送 HTTP 头部
    // HTTP 状态值: 200 : OK
    // 内容类型: text/plain
    response.writeHead(200, {'Content-Type': 'text/plain'});

    // 发送响应数据 "Hello World"
    response.end('Hello World12 ,' +
        '构建成功\n');
}).listen(8086);

// 终端打印如下信息
console.log('1 2 3 4 5 6 7 8 9 12 13 14 Server running at http://127.0.0.1:8086/');