from http.server import BaseHTTPRequestHandler
import urllib
import json
import requests

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_error(415, 'Only post is supported')

    def do_POST(self):
        path = self.path
        #获取post提交的数据
        datas = self.rfile.read(int(self.headers['content-length']))
        datas = urllib.unquote(datas).decode("utf-8", 'ignore')
        
        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.send_header("test","This is test!")
        self.end_headers()
        buf = '''<!DOCTYPE HTML>
        <html>
            <head><title>Post page</title></head>
            <body>Post Data:%s  <br />Path:%s</body>
        </html>'''%(datas,self.path)
        self.wfile.write(buf)

responce = requests.post("https://oss-defense-api.vercel.app/api?text=打卡成功啦！")
print(responce)