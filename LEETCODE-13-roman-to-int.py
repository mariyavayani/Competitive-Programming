# Solution 
class Solution(object):
    def romanToInt(self, s):
        total = 0

        def value(ch):
            if ch == 'I': return 1
            elif ch == 'V': return 5
            elif ch == 'X': return 10
            elif ch == 'L': return 50
            elif ch == 'C': return 100
            elif ch == 'D': return 500
            elif ch == 'M': return 1000
            else: return 0

        for i in range(len(s) - 1):
            if value(s[i]) < value(s[i + 1]):
                total -= value(s[i])
            else:
                total += value(s[i])

        total += value(s[-1])
        return total
