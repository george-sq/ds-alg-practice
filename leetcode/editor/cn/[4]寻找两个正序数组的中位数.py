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

# 解法 1
# def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#     ret_val = 0.0
#     len_1 = len(nums1)
#     len_2 = len(nums2)
#     sum_len = len_1 + len_2
#     counter = 0
#     l_all = []
#     # nums1 为空
#     if 0 == len_1:
#         l_all.extend(nums2)
#         counter = sum_len
#     # nums2 为空
#     if 0 == len_2:
#         l_all.extend(nums1)
#         counter = sum_len
#     # 合并的 正序数组
#     idx_1, idx_2 = 0, 0
#     while counter != sum_len:
#         # 列表1 取数完毕
#         if idx_1 == len_1:
#             l_all.extend(nums2[idx_2:])
#             break
#             pass
#         # 列表2 取数完毕
#         if idx_2 == len_2:
#             l_all.extend(nums1[idx_1:])
#             break
#             pass
#         # 开始对比数组，进行取数
#         if nums1[idx_1] < nums2[idx_2]:
#             l_all.append(nums1[idx_1])
#             idx_1 += 1
#             pass
#         else:
#             l_all.append(nums2[idx_2])
#             idx_2 += 1
#             pass
#         counter += 1
#     idx_m = (sum_len - 1) // 2
#     if 0 == sum_len % 2:
#         ret_val = (l_all[idx_m] + l_all[idx_m + 1]) / 2
#     else:
#         ret_val = l_all[idx_m]
#     return ret_val


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ret_val = 0.0
        len_1 = len(nums1)
        len_2 = len(nums2)
        sum_len = len_1 + len_2
        counter = 0
        l_all = []
        # nums1 为空
        if 0 == len_1:
            l_all.extend(nums2)
            counter = sum_len
        # nums2 为空
        if 0 == len_2:
            l_all.extend(nums1)
            counter = sum_len
        # 合并的 正序数组
        idx_1, idx_2 = 0, 0
        while counter != sum_len:
            # 列表1 取数完毕
            if idx_1 == len_1:
                l_all.extend(nums2[idx_2:])
                break
                pass
            # 列表2 取数完毕
            if idx_2 == len_2:
                l_all.extend(nums1[idx_1:])
                break
                pass
            # 开始对比数组，进行取数
            if nums1[idx_1] < nums2[idx_2]:
                l_all.append(nums1[idx_1])
                idx_1 += 1
                pass
            else:
                l_all.append(nums2[idx_2])
                idx_2 += 1
                pass
            counter += 1
        idx_m = (sum_len - 1) // 2
        if 0 == sum_len % 2:
            ret_val = (l_all[idx_m] + l_all[idx_m + 1]) / 2
        else:
            ret_val = l_all[idx_m]
        return ret_val
# leetcode submit region end(Prohibit modification and deletion)


def app():
    solution = Solution()
    l_nums_1 = [1, 2, 3, 4]
    l_nums_2 = []
    result = solution.findMedianSortedArrays(l_nums_1, l_nums_2)
    print(result)
    pass


if __name__ == "__main__":
    app()
    pass
