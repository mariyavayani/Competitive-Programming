# Link to problem: https://leetcode.com/problems/sqrtx/
# Time Complexity: O(log x) 
# Space Complexity: O(1)
# Approach: Binary search for floor(sqrt(x)) in range [1, x]
# Solution: 
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0 or x==1:
            return x
        left=1
        right=x
        while left<=right:
            mid=(left+right)//2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left=mid+1
            else:
                right=mid-1
        return right
