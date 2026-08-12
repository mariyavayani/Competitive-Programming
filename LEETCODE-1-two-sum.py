# link to problem: https://leetcode.com/problems/two-sum/description/
# Approach: Brute force — check every pair of elements for the target sum
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# Solution:
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i] + nums[j]) == target:
                    return [i,j]
