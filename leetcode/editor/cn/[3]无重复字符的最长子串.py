from typing import List
from typing import Dict
from typing import Tuple
from typing import Sequence

# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。 
# 
#  示例 1: 
# 
#  输入: "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
#  
# 
#  示例 2: 
# 
#  输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
#  
# 
#  示例 3: 
# 
#  输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#  
#  Related Topics 哈希表 双指针 字符串 Sliding Window
# def lengthOfLongestSubstring(self, s: str) -> int:
#     ret_val = 0
#     l_w = []
#     if s:
#         for n in s:
#             if n in l_w:
#                 ret_val = len(l_w) if len(l_w) > ret_val else ret_val
#                 while n in l_w:
#                     l_w.pop(0)
#                     pass
#                 pass
#             l_w.append(n)
#             pass
#         pass
#     return max(ret_val, len(l_w))


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        lookup = set()
        left = 0
        max_len = 0
        cur_len = 0
        for i in range(n):
            cur_len += 1
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
            if cur_len > max_len:
                max_len = cur_len
            lookup.add(s[i])
        return max_len
# leetcode submit region end(Prohibit modification and deletion)


def app():
    solution = Solution()
    s = "abcabcbb"
    result = solution.lengthOfLongestSubstring(s)
    print(result)
    pass


if __name__ == "__main__":
    app()
    pass
