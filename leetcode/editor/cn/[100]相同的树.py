from typing import List
from typing import Dict
from typing import Tuple
from typing import Sequence

# 给定两个二叉树，编写一个函数来检验它们是否相同。 
# 
#  如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。 
# 
#  示例 1: 
# 
#  输入:       1         1
#           / \       / \
#          2   3     2   3
# 
#         [1,2,3],   [1,2,3]
# 
# 输出: true 
# 
#  示例 2: 
# 
#  输入:      1          1
#           /           \
#          2             2
# 
#         [1,2],     [1,null,2]
# 
# 输出: false
#  
# 
#  示例 3: 
# 
#  输入:       1         1
#           / \       / \
#          2   1     1   2
# 
#         [1,2,1],   [1,1,2]
# 
# 输出: false
#  
#  Related Topics 树 深度优先搜索 
#  👍 407 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        ret_val = False
        if q.left is not None and p.left is not None:
            return self.isSameTree(p.left, q.left)
            pass
        if p.right is not None and q.right is not None:
            return self.isSameTree(p.right, q.right)
            pass
        if p.left is None and q.left is None:
            pass
        if p.right is None and q.right is None:
            pass

        if q.val == p.val:
            ret_val = True
            pass
        pass
        return ret_val

        
# leetcode submit region end(Prohibit modification and deletion)


def app():
    solution = Solution()
    result = ""
    print(result)
    pass


if __name__ == "__main__":
    app()
    pass
