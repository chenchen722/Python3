# 1、socket_TCP网络通信

    # socket ：套接字（直译）， 用来实现网络编程的只用数据传输手段

    # socket 把一些复杂的tcp/ip协议进行封装，我们就按部就班遵守socket规则进行编程

    # tcp协议：是传输可靠的数据通信协议（三次握手，四次挥手）
    # 一般用于网络通信安全完整性比较高的时候：邮箱，传输文件， 浏览网页，下载学习视频

    # udp协议：是传输不可靠的数据：会丢包

    # 当实时性要求高的时候,直播，视频，语言

# 通信步骤：
# 1.硬件支持
# 2.传输信息
# 3.关闭链接



# 变成python实现步骤
# 1.建立服务端socket对象
# 2.绑定自己的ip(个人地址)以及端口号（动态端口号：1024-65535）
# 3.建立监听模式，设置最大的链接数
# 4.等待客户端
# 5.接受客户端的数据/给客户端发送信息
# 6.关闭链接




# 客户端
# 1.创建客户端socket 对象
# 2.链接服务端ip和端口号
# 3.接收服务端数据/发送客户端信息
# 4.关闭




# 1.建立服务端socket对象   socket 是内置模块，不需要下载
import socket 
"""
socket 是套接字类，有两个参数

socket_family : 网络地址类型:ipv4参数值 -》 AF_INET
                            ipv6参数值 -》 AF_INET6
                            
socket_type : 协议类型: TCP -->  SOCK_STREAM
                       UDP -->  SOCK_DGRAM
"""

# 实例化套接字对象

# 我们用常规的ipv4,tcp协议的套接字对象
# socket.socket(socket_family, socket_type)
IPhone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定自己的ip和端口号，注意这里是只有一个参数值，但如何传入两个参数？ 需要用元组封装
IPhone.bind( ("127.0.0.1", 8848) )

# 我建立监听模式
IPhone.listen(5)   #最多有五个人链接我  其他人不连接 或者在排队

# 等待客户端的链接

"""
    accept : 这个方法调用会有两个返回值
        1. 客户端对象，这个对象是要用来进行接受和发送的
        2.客户端ip和端口
        
"""

# conn: 客户端对象
# adder: 客户端ip和端口
conn, adder = IPhone.accept()

while 1:
    
    try :
        """
            UDP不需要额外建立链接,只需要接受成功了就可以建立链接
            recvfrom : 也要最大字节数
            
            data :客户端的数据包
            adder : 端口号和ip地址
        
        """
        # 5.接受客户端的数据/给客户端发送信息
        # 接受数据：设定最大字节数，单位为b
        data = conn.recv(1024*1024 )

        # 我们的数据在网络中数据是以数据流传输
        # 我们需要编译为文档文字，decode是字符串的编译
        print(data.decode("utf-8"))

        # 发送信息
        data = input(">>>")
        # 这些需要转译为二进制
        conn.send(data.encode("utf-8"))

    except ConnectionResetError as massg:
        print(massg)
        break

IPhone.close()