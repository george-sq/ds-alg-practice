from typing import List
from typing import Dict
from typing import Tuple
from typing import Sequence

# 幂集。编写一种方法，返回某集合的所有子集。集合中不包含重复的元素。 
# 
#  说明：解集不能包含重复的子集。 
# 
#  示例: 
# 
#   输入： nums = [1,2,3]
#  输出：
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
#  
#  Related Topics 位运算 数组 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        else:
            l_subsets = []
            for element in nums:
                for i in range(len(l_subsets)):
                    l_temp = []
                    l_temp.extend(l_subsets[i])
                    if element not in l_temp:
                        l_temp.append(element)
                        l_subsets.append(l_temp)
                        pass
                    pass
                # 添加 单一元素 的子集
                l_subsets.append([element])
                pass
            l_subsets.append([])
            return l_subsets
            pass
        pass
# leetcode submit region end(Prohibit modification and deletion)


def app():
    solution = Solution()
    nums = [1, 2, 3]
    result = solution.subsets(nums)
    print(result)
    pass


if __name__ == "__main__":
    app()
    pass
