from http.server import BaseHTTPRequestHandler
import urllib
import json
import requests

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_error(415, 'Only post is supported')

    def do_POST(self):
        path = str(self.path)     #获取请求的url
        datas = self.rfile.read(int(self.headers['content-length']))
        datas = urllib.unquote(datas).decode("utf-8", 'ignore')
        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.send_header("test",datas)
        self.end_headers()
        self.wfile.write(json.dumps(datas, ensure_ascii=False).encode())

responce = requests.post("https://oss-defense-api.vercel.app/api")
print(responce.json())