from http.server import BaseHTTPRequestHandler
import urllib
import json
import requests

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_error(415, 'Only post is supported')

    def do_POST(self):
        enc = "UTF-8"              #设置返回的编码格式
        path = str(self.path)     #获取请求的url
        length = int(self.headers.getheader('content-length'))  #获取除头部后的请求参数的长度
        datas = urllib.urlparse.parse_qs(self.rfile.read(length), keep_blank_values=1)  #获取请求参数数据，请求数据为json字符串
        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.send_header("test",datas)
        self.end_headers()
        self.wfile.write(json.dumps(datas, ensure_ascii=False).encode())

responce = requests.post("https://oss-defense-api.vercel.app/api")
print(responce)