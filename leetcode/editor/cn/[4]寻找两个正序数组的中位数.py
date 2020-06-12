from typing import List
from typing import Dict
from typing import Tuple
from typing import Sequence

# 给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。 
# 
#  请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。 
# 
#  你可以假设 nums1 和 nums2 不会同时为空。 
# 
#  
# 
#  示例 1: 
# 
#  nums1 = [1, 3]
# nums2 = [2]
# 
# 则中位数是 2.0
#  
# 
#  示例 2: 
# 
#  nums1 = [1, 2]
# nums2 = [3, 4]
# 
# 则中位数是 (2 + 3)/2 = 2.5
#  
#  Related Topics 数组 二分查找 分治算法


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ret_val = 0.0
        len_1 = len(nums1)
        len_2 = len(nums2)
        total_len = len_1 + len_2
        half_len = total_len / 2
        max_len = max(len_1, len_2)
        l_temp = []
        # 构建合并的 正序数组

        # 计算中位数
        if 0 == total_len % 2:
            ret_val = (l_temp[-1] + l_temp[-2]) / 2
            pass
        else:
            ret_val = float(l_temp[-1])
            pass
        pass
        return ret_val
# leetcode submit region end(Prohibit modification and deletion)


def app():
    solution = Solution()
    l_nums_1 = [1, 2]
    l_nums_2 = [3, 4]
    result = solution.findMedianSortedArrays(l_nums_1, l_nums_2)
    print(result)
    pass


if __name__ == "__main__":
    app()
    pass
