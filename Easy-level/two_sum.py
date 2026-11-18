"""
Tags: Junior - Array - Hash Table

You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_table = {}
        for i, n in enumerate(nums):
            nums_table[n] = i
       
        for i, n in enumerate(nums):
            a = target - n
            if a in nums_table and nums_table[a] != i:
                return [i, nums_table[a]]

# The brut-force method iterates every element of the array with eachother to compare
# if the sum of those two equals to the 'target'
# The optimised version stores the array in a hash table and iterates the array again asking
# "What is the complement of 'b'" aka 'a', then ask "is a inside the table? and is the index
# of 'a' NOT the same as the current index" since the key is the number and the value is their index in nums[]
# optimising it from a 0(n²) to O(n) since it only itterates the full array twice 

solution = Solution()
NUMS = [2, 7, 11, 15]
TARGET = 9
print(solution.twoSum(NUMS, TARGET))