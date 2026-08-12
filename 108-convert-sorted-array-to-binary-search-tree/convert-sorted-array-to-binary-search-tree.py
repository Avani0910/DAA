# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def helper(self, arr, start, end):
        if(start > end):
            return None
        mid = start + (end - start)//2
        root = TreeNode(arr[mid])
        root.left = self.helper(arr, start, mid-1)
        root.right = self.helper(arr, mid+1, end)
        return root
    def sortedArrayToBST(self, nums):
        return self.helper(nums, 0, len(nums)-1)        

        
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        