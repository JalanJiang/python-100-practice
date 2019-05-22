# Day07 - 字符串和常用数据结构

## 字符串

### 切片

- [廖雪峰 Python 切片](https://www.liaoxuefeng.com/wiki/897692888725344/923029651584288)

```Python
str2 = 'abc123456'
# 从字符串中取出指定位置的字符(下标运算)
print(str2[2])  # c
# 字符串切片(从指定的开始索引到指定的结束索引)
print(str2[2:5])  # c12
print(str2[2:])  # c123456
print(str2[2::2])  # c246
print(str2[::2])  # ac246
print(str2[::-1])  # 654321cba
print(str2[-3:-1])  # 45
```

## 列表

- 排序
    - `list = sorted(list)` 返回排序后的结果
    - `list.sort()` 直接在列表对象上排序
- [列表生成式](https://www.liaoxuefeng.com/wiki/897692888725344/923029657876192)
