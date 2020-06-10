from typing import List
from typing import Dict
from typing import Tuple
from typing import Sequence

# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。 
# 
#  如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。 
# 
#  您可以假设除了数字 0 之外，这两个数都不会以 0 开头。 
# 
#  示例： 
# 
#  输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
#  输出：7 -> 0 -> 8
#  原因：342 + 465 = 807
#  
#  Related Topics 链表 数学


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        cur = head
        carry = 0
        while l1 or l2:
            x = l1.val if isinstance(l1, ListNode) and 0 < l1.val else 0
            y = l2.val if isinstance(l2, ListNode) and 0 < l2.val else 0
            num_sum = x + y + carry
            # 是否有进位
            carry = num_sum // 10
            val = num_sum % 10
            # 创建 求和 节点
            cur.next = ListNode(val)
            # 移动 链表指针
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            cur = cur.next
            pass
        if 0 < carry:
            cur.next = ListNode(carry)
            pass
        pass
        return head.next
# leetcode submit region end(Prohibit modification and deletion)


def app():
    solution = Solution()
    a = [2, 4, 3]
    b = [5, 6, 4]
    result = ""
    print(result)
    pass


if __name__ == "__main__":
    app()
    pass
