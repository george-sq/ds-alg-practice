# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。 
# 
#  你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。 
# 
#  
# 
#  示例: 
# 
#  给定 nums = [2, 7, 11, 15], target = 9
# 
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
#  
#  Related Topics 数组 哈希表


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def twoSum(self, nums, target):
        ret_val = []
        # 暴力方法
        # for i, element_i in enumerate(nums):
        #     for j, element_j in enumerate(nums[i+1:]):
        #         if target == (element_i + element_j):
        #             ret_val.append(i)
        #             ret_val.append(i + j + 1)
        #             pass
        #         pass
        #     pass
        # pass

        # 优化方法
        d_map = {}
        for idx, val in enumerate(nums):
            if val not in d_map.keys():
                val_another = target - val
                d_map[val_another] = idx
            else:
                ret_val = [d_map[val], idx]
                pass
            pass
        return ret_val

# leetcode submit region end(Prohibit modification and deletion)


def app():
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    result = solution.twoSum(nums, target)
    print(result)
    pass


if __name__ == "__main__":
    app()
    pass
