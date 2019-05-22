"""
完美数是除自身外其他所有因子的和正好等于这个数本身的数
来自 LeetCode: 507. 完美数

Version: 1.0.0
Author: Jalan
Date: 2019-05-22
"""

import math

class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        if num <= 1:
            return False
        
        s = 0
        for factor in range(1, int(math.sqrt(num)) + 1):
            # 判断是否是因子
            if num % factor == 0:
                s += factor
                # 避免相同因子重复添加
                if factor != 1 and num / factor != factor:
                    s += num / factor
            
        if s == num:
            return True
        else:
            return False