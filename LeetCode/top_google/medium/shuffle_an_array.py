'''
    https://leetcode.com/problems/shuffle-an-array/

    384. Shuffle an Array

    Given an integer array nums, design an algorithm to randomly shuffle the array. All permutations of the array should be equally
    likely as a result of the shuffling.

    Implement the Solution class:
        - Solution(int[] nums) Initializes the object with the integer array nums.
        - int[] reset() Resets the array to its original configuration and returns it.
        - int[] shuffle() Returns a random shuffling of the array.
'''
'''
    Accepted
    
    Note: we could also use the Fisher-Yates algorithm where at each iteration, we choose a random index between i and the end of the array
    and then swap nums[i] with nums[random_index]. The good thing about this solution is that we shuffle the array in place.
    However, since the Solution also requires a reset() function, then there's no point in using the Fisher-Yates algorithm since we always
    need a copy of the original array to return when reset() is called.
'''
import random


class Solution:
    nums = []

    def __init__(self, nums: [int]):
        self.nums = nums

    def reset(self) -> [int]:
        return self.nums

    def shuffle(self) -> [int]:
        shuffled_array = []
        used = set()

        while len(shuffled_array) != len(self.nums):
            num = random.choice(self.nums)

            if num not in used:
                used.add(num)
                shuffled_array.append(num)

        return shuffled_array


nums = [1, 2, 3]
# Your Solution object will be instantiated and called as such:
obj = Solution(nums)
print(obj.shuffle())
print(obj.reset())
print(obj.shuffle())
