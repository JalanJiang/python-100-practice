"""
英制单位英寸和公制单位厘米互换
1英寸(in) = 2.54厘米(cm)

输入：长度 value 与 单位 unit
输出：另外一类的长度与单位

Version: 1.0.0
Author: Jalan
"""

value = float(input("请输入长度："))
unit = input("请输入单位：")

# 如果输入的是厘米
if unit == "cm" or unit == "厘米":
    output_value = value / 2.54
    print("%f 厘米 = %f 英寸" % (value, output_value))
# 如果输入的是英寸
elif unit == "in" or unit == "英寸":
    output_value = value * 2.54
    print("%f 英寸 = %f 厘米" % (value, output_value))
# 输入的单位无效
else:
    print("请输入有效单位")