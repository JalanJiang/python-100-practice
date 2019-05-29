# Day14A - 网络编程入门

## 计算机网络

- 网络协议三大要素：语法、语义、时序
- TCP/IP 四层模型，自底向上分别是：
  - 网络接口层
  - 网络层：IP 协议服务于该层，用于寻址和路由
  - 传输层
  - 应用层
- 路由功能：存储转发我们发送到网络上的数据分组，让从源头发出的数据最终能够找到传送到目的地同路
- TCP 的可靠性：
  1. 数据不传丢不传错（利用握手、校验和重传机制可以实现）
  2. 流量控制（通过滑动窗口匹配数据发送者和接收者之间的传输速度）
  3. 拥塞控制（通过RTT时间以及对滑动窗口的控制缓解网络拥堵）

## 基于传输层协议的套接字编程

套接字就是一套用C语言写成的应用程序开发库，主要用于实现进程间通信和网络编程，在网络应用开发中被广泛使用。

### TCP 套接字

TCP 套接字就是使用 TCP 协议提供的传输服务来实现网络通信的编程接口。

在 Python 中：

- 创建 `socket` 对象
- 指定 `type` 属性为 `SOCK_STREAM`

#### 实现服务器程序

```python
from socket import socket, SOCK_STREAM, AF_INET
from datetime import datetime


def main():
    # 1.创建套接字对象并指定使用哪种传输服务
    # family=AF_INET - IPv4地址
    # family=AF_INET6 - IPv6地址
    # type=SOCK_STREAM - TCP套接字
    # type=SOCK_DGRAM - UDP套接字
    # type=SOCK_RAW - 原始套接字
    server = socket(family=AF_INET, type=SOCK_STREAM)
    # 2.绑定IP地址和端口(端口用于区分不同的服务)
    # 同一时间在同一个端口上只能绑定一个服务否则报错
    server.bind(('192.168.1.2', 6789))
    # 3.开启监听 - 监听客户端连接到服务器
    # 参数512可以理解为连接队列的大小
    server.listen(512)
    print('服务器启动开始监听...')
    while True:
        # 4.通过循环接收客户端的连接并作出相应的处理(提供服务)
        # accept方法是一个阻塞方法如果没有客户端连接到服务器代码不会向下执行
        # accept方法返回一个元组其中的第一个元素是客户端对象
        # 第二个元素是连接到服务器的客户端的地址(由IP和端口两部分构成)
        client, addr = server.accept()
        print(str(addr) + '连接到了服务器.')
        # 5.发送数据
        client.send(str(datetime.now()).encode('utf-8'))
        # 6.断开连接
        client.close()


if __name__ == '__main__':
    main()
```

运行时：

```
telnet 192.168.1.2 6789
```

#### 实现客户端程序

```python
from socket import socket


def main():
    # 1.创建套接字对象默认使用IPv4和TCP协议
    client = socket()
    # 2.连接到服务器(需要指定IP地址和端口)
    client.connect(('192.168.1.2', 6789))
    # 3.从服务器接收数据
    print(client.recv(1024).decode('utf-8'))
    client.close()


if __name__ == '__main__':
    main()
```

### UDP 套接字

与 TCP 的区别：

- UDP 不对传输的可靠性和可达性做保证
- 避免了 TCP 握手和重传的开销
- 强调性能而不是数据完整性的场景可用 UDP

### 原始套接字

## 其他

### 关于端口

- 端口取值范围是 0~65535
- 1024 下的端口称之为“著名端口”或“周知端口”（留给 FTP HTTP SMTP 等著名服务使用的端口）
- 自定义的服务通常不使用“著名端口”