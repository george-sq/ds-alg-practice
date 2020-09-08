from typing import List
from typing import Dict
from typing import Tuple
from typing import Sequence

# 给定一个二叉树，返回它的 前序 遍历。 
# 
#  示例: 
# 
#  输入: [1,null,2,3]  
#    1
#     \
#      2
#     /
#    3 
# 
# 输出: [1,2,3]
#  
# 
#  进阶: 递归算法很简单，你可以通过迭代算法完成吗？ 
#  Related Topics 栈 树 
#  👍 359 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ret_list = []
        if root:
            if root.val:
                ret_list.append(root.val)
                pass
            if root.left is not None:
                ret_list.extend(self.preorderTraversal(root.left))
                pass
            if root.right is not None:
                ret_list.extend(self.preorderTraversal(root.right))
                pass
            pass
        else:
            pass
        pass
        return ret_list
# leetcode submit region end(Prohibit modification and deletion)


def app():
    solution = Solution()
    result = ""
    print(result)
    pass


if __name__ == "__main__":
    app()
    pass