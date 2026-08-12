# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        n = 0
        cur = head
        while cur :
            cur = cur.next
            n += 1
        self.head = head
        def rec(start, end):
            if start>end:
                return None
            mid = (start + end)//2
            left = rec(start, mid - 1)
            root = TreeNode(self.head.val)
            self.head = self.head.next
            root.left = left
            root.right = rec(mid + 1, end)
            return root
        return rec(0,n - 1)   

        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        