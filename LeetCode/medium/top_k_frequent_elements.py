'''
    https://leetcode.com/problems/top-k-frequent-elements/

    347. Top K Frequent Elements

    Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
'''

'''
    Accepted: Similar to Heap approach in solution but instead of using a Heap to sort the counts, we use python's sorting algorithm
    
    In the heap approach, to avoid O(n log n), they cater for the case where k = n separately so we will do this in Solution 2.
'''


class Solution:
    def topKFrequent(self, nums: [int], k: int) -> [int]:
        counts = {}

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        counts = sorted(counts.items(), key=lambda item: item[1], reverse=True)

        result = []

        for i in range(0, k):
            result.append(counts[i][0])

        return result


'''
    Accepted
'''


class Solution2:
    def topKFrequent(self, nums: [int], k: int) -> [int]:
        # k which is maximum number of UNIQUE elements in array is equal to number of elements in the array
        # this means that all the elements in the array are unique => all have same frequency = 1
        # so we just return nums in this case
        if k == len(nums):
            return nums

        counts = {}

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        counts = sorted(counts.items(), key=lambda item: item[1], reverse=True)

        result = []

        for i in range(0, k):
            result.append(counts[i][0])

        return result


import random

'''
    Accepted
    
    Approach 2: Quickselect (Hoare's selection algorithm)
'''


class Solution3:
    # we will use the Select algorithm to get the answer we want
    # however, when we're partitioning the array, we won't rely on the current element's value
    # we will instead used its frequency

    def partition(self, unique, count, left, right, pivot_index):
        pivot_frequency = count[unique[pivot_index]]

        # move the pivot to the end
        unique[pivot_index], unique[right] = unique[right], unique[pivot_index]

        i = left - 1

        for j in range(left, right):
            # NOTE difference between mine and theirs is that mine was <=
            # need to move all the elements that are STRICTLY less than frequency of pivot to the left => not less than or equal
            if count[unique[j]] < pivot_frequency:
                i += 1
                unique[j], unique[i] = unique[i], unique[j]

        # put the pivot in the last place in the array and now we need to put it in its rightful place
        unique[right], unique[i + 1] = unique[i + 1], unique[right]

        return i + 1

    def select(self, unique, count, left, right, kth_less_frequent):
        if left == right:
            # we have one element in the subarray
            return unique[left]

        pivot_index = random.randint(left, right)

        pivot_index = self.partition(unique, count, left, right, pivot_index)

        # here I was comparing kth_smallest to k but instead we need to compare kth_smallest with pivot_index
        if kth_less_frequent == pivot_index:
            # it means that we need the kth element which is A[q] [since indexing starts at 0]
            return unique[pivot_index]
        elif kth_less_frequent < pivot_index:
            # if kth_less_frequent element is less than the index of our current pivot, it means that to look for the kth_less_frequent
            # we need to look BEFORE pivot_index so we go to the left because all elements less frequent than pivot_index are to its left
            return self.select(unique, count, left, pivot_index - 1, kth_less_frequent)
        else:
            # we go right
            return self.select(unique, count, pivot_index + 1, right, kth_less_frequent)

    def topKFrequent(self, nums: [int], k: int) -> [int]:
        count = {}

        for num in nums:
            if num not in count:
                count[num] = 0

            count[num] += 1

        # we can't keep duplicates in the array because the selection algorithm won't work then
        unique = list(set(nums))

        n = len(unique)

        # kth top frequent element is (n - k)th less frequent.
        # Do a partial sort: from less frequent to the most frequent, till
        # (n - k)th less frequent element takes its place (n - k) in a sorted array.
        # All element on the left are less frequent.
        # All the elements on the right are more frequent.
        self.select(unique, count, 0, n - 1, n - k)

        return unique[n - k:]


nums = [1, 1, 1, 2, 2, 3]
k = 2

# nums = [1]
# k = 1
#
# nums = [1,2]
# k = 2

print(Solution3().topKFrequent(nums, k))
