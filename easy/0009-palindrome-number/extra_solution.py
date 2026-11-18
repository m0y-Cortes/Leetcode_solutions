"""
Alternative solution: Not usign strings
"""
class SolutionB:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and  x != 0):
            return False
        inverted_half = 0
        while x > inverted_half:
            x, d = divmod(x, 10)
            inverted_half = inverted_half * 10 + d
        return x == inverted_half or x == inverted_half // 10

# This does not optimises time, but storage since a int is smaller than a str in size
# This aproach "pops" the last digit of x using divmod (returns the '% 10' of x and divides it by 10)
# and adds it to inverted_half, like having a strip with the number ans stripping the last digit
# adding them to a new strip and matching them. In case the lenght is inpair the inverted_half
# keeps the middle digit and when comparing its divided by floor 10 deleting that irrelevant-for-the-comparison digit

solution = SolutionB()
X = 2345432
print(solution.isPalindrome(X))