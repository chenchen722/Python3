# 客户端
# 1.创建客户端socket 对象
# 2.链接服务端ip和端口号
# 3.接收服务端数据/发送客户端信息
# 4.关闭

# 1.创建客户端socket 对象

import socket


# 创建客户端socket 对象
# 这个参数值必须和服务端一致
hank = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2.链接服务端ip和端口号
# 服务端ip和端口号
hank.connect( ("127.0.0.1", 8848) )

while 1:
    data = input(">>>")

    hank.send(data.encode("utf-8"))
    
    if data == "晚安":
        break

    if not data:
        continue



    # 这里设置数据接受的最大字节数
    data = hank.recv(1024)

    print(data.decode("utf-8"))

hank.close()



