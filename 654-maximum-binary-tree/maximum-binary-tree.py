# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        return self.build(nums, 0, len(nums) - 1)
        
    def build(self, nums, left, right):
            
        
        if left > right:
            return None
        max_index = left
        for i in range(left , right+1):
            if nums[i] > nums[max_index]:
                max_index = i
        root = TreeNode(nums[max_index])
        root.left = self.build(nums, left, max_index - 1)
        root.right = self.build(nums, max_index + 1, right)

        return root
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        