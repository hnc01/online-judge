'''
    https://leetcode.com/problems/kth-largest-element-in-an-array/

    215. Kth Largest Element in an Array

    Given an integer array nums and an integer k, return the kth largest element in the array.

    Note that it is the kth largest element in the sorted order, not the kth distinct element.
'''

'''
    Accepted
'''


class Solution:
    def partition(self, A, p, r):
        x = A[r]

        i = p - 1

        for j in range(p, r):
            if A[j] <= x:
                i += 1
                temp = A[j]
                A[j] = A[i]
                A[i] = temp

        temp = A[r]
        A[r] = A[i + 1]
        A[i + 1] = temp

        return i + 1

    def select(self, A, p, r, i):
        # if the array is made up of one element then we return that element
        if p == r:
            return A[p]

        # otherwise we partition the array around a pivot which we take to be the last element in current subarray
        q = self.partition(A, p, r)

        # the pivot element is at index q

        # k = number of elements in the second part of the partition (i.e. elements greater than q)
        k = r - q + 1

        if i == k:
            # we found the kth smallest/largest element
            return A[q]
        elif i < k:
            # we need to look to the right
            return self.select(A, q + 1, r, i)
        else:
            # we need to look to right
            return self.select(A, p, q - 1, i - k)

    def findKthLargest(self, nums: [int], k: int) -> int:
        return self.select(nums, 0, len(nums) - 1, k)


nums = [3, 2, 1, 5, 6, 4]
k = 1

nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4

print(Solution().findKthLargest(nums, k))
