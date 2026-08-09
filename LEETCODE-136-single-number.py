# Link to problem: https://leetcode.com/problems/single-number/
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: XOR all elements — duplicates cancel out (a^a=0), leaving the single number
# Solution
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index=0
        for num in nums:
            index=index^num
        return index
