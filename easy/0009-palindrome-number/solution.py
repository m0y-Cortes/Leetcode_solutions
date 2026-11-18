"""
Given an integer x, return true if x is a palindrome, and false otherwise.

If a integer is negative ot must yield FALSE (-121 != 121-)
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and  x != 0):
            return False
        num_string = str(x)
        for i in range (len(num_string)//2):
            if num_string[i] != num_string[-(i+1)]:
                return False
        return True

# Before convert the integer into a string and read it checks for cases that are 100%
# NOT palindromes (negative numbers or multiples of 10)
# Reads the starts and the end of the string moving towards the middle, and after reaching
# the middle stops (ignoring the exact middle number if the lenght is inpair) instead of
# repeating the same path the other side passed. If any check doesn't match returns false.
# With a final 

solution = Solution()
X = 2345432
print(solution.isPalindrome(X))