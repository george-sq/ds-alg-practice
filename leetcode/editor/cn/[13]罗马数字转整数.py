from typing import List
from typing import Dict
from typing import Tuple
from typing import Sequence

# 罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。 
# 
#  字符          数值
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000 
# 
#  例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做 XXVII, 即为 XX + V + I
# I 。 
# 
#  通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5
#  减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况： 
# 
#  
#  I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。 
#  X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
#  C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。 
#  
# 
#  给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。 
# 
#  示例 1: 
# 
#  输入: "III"
# 输出: 3 
# 
#  示例 2: 
# 
#  输入: "IV"
# 输出: 4 
# 
#  示例 3: 
# 
#  输入: "IX"
# 输出: 9 
# 
#  示例 4: 
# 
#  输入: "LVIII"
# 输出: 58
# 解释: L = 50, V= 5, III = 3.
#  
# 
#  示例 5: 
# 
#  输入: "MCMXCIV"
# 输出: 1994
# 解释: M = 1000, CM = 900, XC = 90, IV = 4. 
#  Related Topics 数学 字符串


# leetcode submit region begin(Prohibit modification and deletion)
def m_1(s):
    # print(s)
    d = {
        'I': 1, 'IV': 3, 'V': 5, 'IX': 8,
        'X': 10, 'XL': 30, 'L': 50, 'XC': 80,
        'C': 100, 'CD': 300, 'D': 500,
        'CM': 800, 'M': 1000
    }
    # l_nums = []
    # for i, n in enumerate(s):
    #     t = i - 1
    #     start = max(t, 0)
    #     end = i + 1
    #     a = s[start: end]
    #     val = d.get(a, d[n])
    #     print(f"i={i}, start={start}, end={end}, a={a}, n={n}, val={val}")
    #     l_nums.append(val)
    #     pass
    l_nums = [d.get(s[max(i - 1, 0):i + 1], d[n]) for i, n in enumerate(s)]
    pass
    return sum(l_nums)


def m_2(str_some):
    # print(str_some)
    d = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    l_nums = []
    len_str = len(str_some)
    for i in range(len_str):
        val = d.get(str_some[i], 0)
        val_next = d.get(str_some[i + 1], 0) if len_str > (i + 1) else 0
        # print(f"val={val}, val_next={val_next}")
        val = val if val >= val_next else 0 - val
        l_nums.append(val)
        pass
    pass
    # print(l_nums)
    # l_nums = [d.get(str_some[i], 0) if d.get(str_some[i], 0) >= d.get(str_some[i+1], 0) else -d.get(str_some[i], 0) for i in range(len_str) if len_str > (i + 1)]
    # l_nums.append(d.get(str_some[-1], 0))
    return sum(l_nums)


class Solution:
    def romanToInt(self, s: str) -> int:
        # method 1
        # ret_val = m_1(s)
        # method 2
        ret_val = m_2(s)
        return ret_val
# leetcode submit region end(Prohibit modification and deletion)


def app():
    solution = Solution()
    s = "MCMXCIII"
    result = solution.romanToInt(s)
    print(result)
    pass


if __name__ == "__main__":
    app()
    pass
