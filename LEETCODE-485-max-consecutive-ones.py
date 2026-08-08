link to problem: https://leetcode.com/problems/max-consecutive-ones/
Time Complexity: O(n)
Space Complexity: O(1)

Solution:
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        count1=0
        for num in nums:
            if num==1:
                count=count+1
                if count>count1:
                    count1=count
            else:
                count=0
        return count1
