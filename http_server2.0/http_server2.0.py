"""
主要功能：
1.主要功能
接收客户端（浏览器）请求
解析客户端发送的请求
根据请求组织数据内容
将数据内容形成http响应格式返回给浏览器
2.升级点：
采用IO并发，可以满足多个客户端同时发起请求情况
通过类接口形式进行功能封装
做基本的请求解析，根据具体请求返回请求内容，同时处理客户端的非网页请求行为
"""
class HttpServer:
    pass
if __name__ == '__main__':
    host = '0.0.0.0'
    port = 8888
