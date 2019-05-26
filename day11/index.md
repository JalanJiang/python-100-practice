# Day11 - 文件和异常

## 读写文本

`open()` 函数：

- 文件名
- 操作模式
- 编码（如果不能保证保存文件时使用的编码方式与encoding参数指定的编码方式是一致的，那么就可能因无法解码字符而导致读取失败）

| 操作模式 | 具体含义                         |
| -------- | -------------------------------- |
| `'r'`    | 读取 （默认）                    |
| `'w'`    | 写入（会先截断之前的内容）       |
| `'x'`    | 写入，如果文件已经存在会产生异常 |
| `'a'`    | 追加，将内容写入到已有文件的末尾 |
| `'b'`    | 二进制模式                       |
| `'t'`    | 文本模式（默认）                 |
| `'+'`    | 更新（既可以读又可以写）         |

如何根据应用程序的需要来设置操作模式：

![](/img/day11/file-open-mode.png)

### 方法

- `f.read()` 读取所有
- `f.readlines()` 按行读取
- `for line in f`

### 读写 JSON

Python 的 json 模块。

- `dump` - 将 Python 对象按照 JSON 格式序列化到文件中
- `dumps` - 将 Python 对象处理成 JSON 格式的字符串
- `load` - 将文件中的 JSON 数据反序列化成对象
- `loads` - 将字符串的内容反序列化成 Python 对象

## 异常机制

```python
try:
    pass
except FileNotFoundError:
    pass
except LookupError:
    pass
except UnicodeDecodeError:
    pass
finally:
    # 无论是否有异常最终都会执行
```

## 其他

- 使用 `with` 关键字指定文件对象上下文环境，在离开上下文环境时会自动释放文件资源
- 也可以在 `finally` 中进行 `f.close()`

## 推荐阅读

- [总结：Python中的异常处理](https://segmentfault.com/a/1190000007736783)