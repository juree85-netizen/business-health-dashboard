const http = require('http');
const fs = require('fs');
const path = require('path');

const UPLOAD_DIR = '/home/ubuntu/uploads';
if (!fs.existsSync(UPLOAD_DIR)) fs.mkdirSync(UPLOAD_DIR);

function parseMultipart(body, boundary) {
  const parts = body.split('--' + boundary);
  for (const part of parts) {
    if (!part.includes('filename=')) continue;
    const match = part.match(/filename="([^"]+)"/);
    if (!match) continue;
    const filename = match[1];
    const dataStart = part.indexOf('\r\n\r\n') + 4;
    const dataEnd = part.lastIndexOf('\r\n');
    const fileData = Buffer.from(part.slice(dataStart, dataEnd), 'binary');
    return { filename, fileData };
  }
  return null;
}

const server = http.createServer((req, res) => {
  if (req.method === 'POST' && req.url === '/upload') {
    const ct = req.headers['content-type'] || '';
    const boundaryMatch = ct.match(/boundary=(.+)/);
    if (!boundaryMatch) {
      res.writeHead(400); return res.end('boundary 없음');
    }
    const boundary = boundaryMatch[1];
    const chunks = [];
    req.on('data', chunk => chunks.push(chunk));
    req.on('end', () => {
      const body = Buffer.concat(chunks).toString('binary');
      const result = parseMultipart(body, boundary);
      if (!result) {
        res.writeHead(400); return res.end('파일 파싱 실패');
      }
      const savePath = path.join(UPLOAD_DIR, result.filename);
      fs.writeFileSync(savePath, result.fileData, 'binary');
      res.writeHead(200, { 'Content-Type': 'text/plain; charset=utf-8' });
      res.end(`✅ 업로드 완료: ${result.filename}`);
    });
    return;
  }
  res.writeHead(404); res.end('Not found');
});

server.listen(9090, '127.0.0.1', () => {
  console.log('업로드 서버 실행 중 (localhost:9090)');
});
