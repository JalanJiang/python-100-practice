# Day13 - 进程和线程

## 概念

- 进程分配资源的基本单位
- 一个进程可以包含多个线程
- 线程是调度的基本单位

## 关于fork

- 用来创建进程
- 调用 `fork()` 的是父进程
- 创建出来的是子进程
- 子进程是父进程的一个拷贝，但有自己的 PID
- `fork()` 会返回两次
  - 父进程通过 `fork()` 返回值获取子进程 PID
  - 子进程中的返回值永远是 0

## Python 中的多进程

### 创建进程

- os 模块提供了 `fork()` 函数
- multiprocessing 模块中的 `Process` 类可以用来创建子进程：启动进程 `start` 方法；等待进程执行结束：`join` 方法
  - 批量启动进程的进程池 `Pool`
  - 进程间通信队列 `Queue`
  - 管道 `Pipe`

### 进程间通信

- 使用 multiprocessing 模块中的 `Queue`（底层通过管道和信号量实现）

## Python 中的多线程

- threading 模块
  - 使用 `Tread` 类创建线程
  - 也可以继承 `Thread` 创建自己的线程类

```python
from threading import Thread
```

- Python 多线程并不能发挥 CPU 的多核特性

### 线程间通信

- 线程共享进程的内存空间
- 实现
  - 设置全局变量用于共享
  - 注意“临界资源”的处理问题：加锁，只有获得缩的线程才能访问临界资源

```python
from threading import Lock

lock = Lock()
# 获取锁
lock.acquire()
# 释放锁
lock.release()
```

## 多进程还是多线程

- 无论是多线程还是多进程，数量过多都会导致效率下降
- 操作系统切换线程和进程时需要：
  - 保存现场环境（CPU寄存器状态、内存页等）
  - 新任务的执行环境准备好（恢复上次的寄存器状态，切换内存页等）

## 单进程 + 异步 I/O

- 充分利用操作系统提供的异步 I/O 支持，可以使用单进程单线程执行多任务
- 且看 Nginx
  - 单核 CPU 上采用单进程模型可以有效支持多任务
  - 在多核 CPU 上可以运行多个进程（数量与 CPU 核心数相同）
- 单线程 + 异步 I/O 在 Python 中称为协程
  - 极高的执行效率
  - 子程序切换不是线程切换，而是由程序自身控制，因此没有线程切换的开销
  - 不需要多线程的锁机制。因为只有一个线程

## 案例