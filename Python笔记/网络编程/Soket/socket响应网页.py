# 网页响应需要遵守http协议规则

# 那么http协议格式需要我们来编写的

# 浏览器接受的数据格式为：

# 	响应格式：
# 	1.响应首行（http版本， 响应状态码） HTTP1.1 200 ok  \r\n
# 	2.响应头（一大堆键值对）一般协议服务器版本号，开发组，开发策略.... \r\n
# 	3.空白行 \r\n
# 	4.响应体（需要返回给浏览器看的数据（前端数据））
	
# 	客户端请求格式：
	
# 	不需要，因为你可以直接在浏览器敲链接，浏览器都封装好了
	
	
# b/s端

import socket

if __name__ == '__main__':
    tcpServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 需要设置端口复用，程序检查到关闭链接会直接关端口
    tcpServerSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

    #绑定端口号
    # 你可以这样写""这样子写就是默认本机地址
    tcpServerSocket.bind(("",8848))
    tcpServerSocket.listen(128)

    while 1:
        try:
            newSocket, adder = tcpServerSocket.accept()
            data = newSocket.recv(1024*5)
            # 打印请求数据
            print(data)

            # 设置响应包

            # 响应行
            # HTTP/1.1 是http版本， 200+ok 说明已经请求成功
            responseLine = "HTTP/1.1 200 ok \r\n"

            # 响应头, 可以编写服务器版本
            responseHeader = "server: ZiLingSever/1.0 \r\n"

            # 响应体， 数据包

            with open(r"文件名", "r" , encoding="utf-8") as f:
                responseBody = f.read()


            # 把上面的响应行，响应头，响应体三者合一，变成报文
            response = responseLine+responseHeader+"\r\n"+responseBody

            # 组装好需要转换为二进制
            responseData = response.encode("utf-8")

            newSocket.send(responseData)
            newSocket.close()


        except Exception as e:
            print(e)
            break