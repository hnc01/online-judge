'''
    https://leetcode.com/problems/median-of-two-sorted-arrays/

    4. Median of Two Sorted Arrays

    Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

    The overall run time complexity should be O(log (m+n)).
'''

'''
    Accepted
'''


class Solution:
    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
        # first we check if the total of the 2 is even or odd
        m = len(nums1)
        n = len(nums2)

        if (m + n) % 2 != 0:
            # we have an odd amount of numbers
            target_index_1 = (m + n) // 2
            target_index_2 = (m + n) // 2
            target_median_1 = None
            target_median_2 = None
        else:
            # we have an even amount of numbers
            target_index_1 = ((m + n) // 2) - 1
            target_index_2 = (m + n) // 2
            target_median_1 = None
            target_median_2 = None

        l1 = 0  # will loop over nums1
        l2 = 0  # will loop over nums2

        merged_index = 0  # the current index we would have after merging the lists

        # we keep looping while we still have elements in both arrays
        while l1 < m and l2 < n and (target_median_1 is None or target_median_2 is None):
            if nums1[l1] <= nums2[l2]:
                # we advance in nums1
                if merged_index == target_index_1:
                    target_median_1 = nums1[l1]

                if merged_index == target_index_2:
                    target_median_2 = nums1[l1]

                merged_index += 1
                l1 += 1
            else:
                # we advance in nums2
                if merged_index == target_index_1:
                    target_median_1 = nums2[l2]

                if merged_index == target_index_2:
                    target_median_2 = nums2[l2]

                merged_index += 1
                l2 += 1

        # we could have broken the loop because:
        # 1- one of the arrays is over but the other one has more elements (maybe)
        # 2- we filled both our targets

        while l1 < m and (target_median_1 is None or target_median_2 is None):
            if merged_index == target_index_1:
                target_median_1 = nums1[l1]

            if merged_index == target_index_2:
                target_median_2 = nums1[l1]

            merged_index += 1
            l1 += 1

        while l2 < n and (target_median_1 is None or target_median_2 is None):
            # we advance in nums2
            if merged_index == target_index_1:
                target_median_1 = nums2[l2]

            if merged_index == target_index_2:
                target_median_2 = nums2[l2]

            merged_index += 1
            l2 += 1

        # at this point we're sure that our target median values are filled
        if (m + n) % 2 != 0:
            # we only use target_median_1
            return target_median_1
        else:
            # we use both target medians
            return (target_median_1 + target_median_2) / 2


'''
    Using Binary Search
    
    The idea of the median is that we need to partition the array such that half of the elements are to the right and half are to the left.
    This would leave the median element in the middle. In case of even, we partition the array into half right and half left and the median
    would be the average between the right-most element of left partition and left-most element of right partition.
'''


class Solution2:
    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
        # all we need to do is find our left partition and right partition. The left and right partitions
        # contain the same number of elements where all the elements in the left partition are less than our
        # median and all the elements in the right partition are greater than our median. However, what is fixed
        # is the length of the partitions so we will use that to find them.

        # by finding the elements of nums1 that belong to the left partition, we automatically end up finding
        # the elements of nums2 that belong to the left partition because half - nums1Left = nums2Left, where
        # nums1Left is the number of elements of nums1 belonging to left partition and nums2Left same but for nums2.

        # so, all we need to do is binary search on one of the arrays to find our left partition.
        # Let's say we use nums2 as the array to perform binary search on, if array is the larger array, then when we
        # do half - nums2Left, we might get nums1Left with a value more than we have elements in nums1. Similarly,
        # if we use nums1 as the array to perform binary search one, and it turned out that nums1 is the smaller array
        # we will run into the same problem. So, it's best to do binary search on the smaller array and that way
        # we can guarantee to some degree that half - Left leads to a valid elements count in the other array.
        # We'll choose nums2 as our smaller array and we'll guarantee this by swapping nums1 and num2 if nums2 is larger.

        if len(nums2) > len(nums1):
            nums1, nums2 = nums2, nums1

        # Moving forward, we know that len(nums2) <= len(nums1)
        # we will do binary search on nums2

        m = len(nums1)
        n = len(nums2)

        total = m + n  # total number of elements in merged array
        half = total // 2  # total number of elements in each partition: left and right

        l, r = 0, n - 1

        while True:
            middle = (l + r) // 2  # finding the middle elements of the current portion [l, r] we're looking at out of nums2

            # since we found our middle, the left partition out of nums2 is from 0 to middle => middle - 0 + 1 = number of elements in left part
            nums2LeftSize = middle + 1  # middle - 0 + 1

            # now we need to find the number of elements of nums1 belonging to left partition
            nums1LeftSize = half - nums2LeftSize

            nums2LeftPartitionIndex = middle
            nums1LeftPartitionIndex = nums1LeftSize - 1

            # --> We went back here after the last comment in this code, to handle cases where the indices are out of bounds
            # since for Left indices we always need the max, then to make sure that the out of bounds value is always
            # not considered, we make the out of bounds value as - inf. That way, we never take it when we are looking for max
            nums1LeftPartitionValue = nums1[nums1LeftPartitionIndex] if nums1LeftPartitionIndex >= 0 else float('-inf')
            nums2LeftPartitionValue = nums2[nums2LeftPartitionIndex] if nums2LeftPartitionIndex >= 0 else float('-inf')

            # since for Right indices we always need the min, then to make sure that the out of bounds value is always
            # not considered, we make the out of bounds value as + inf. That way, we never take it when we are looking for min.
            nums1RightPartitionValue = nums1[nums1LeftPartitionIndex + 1] if ((nums1LeftPartitionIndex + 1) < m) else float('inf')
            nums2RightPartitionValue = nums2[nums2LeftPartitionIndex + 1] if ((nums2LeftPartitionIndex + 1) < n) else float('inf')

            # now that we have the indices of the last elements in the left partitions of nums1 and nums2
            # we need to know if the partitions are valid
            # we check for validity by comparing nums1[nums1LeftPartitionIndex] with nums2[nums2LeftPartitionIndex+1]
            # and nums2[nums2LeftPartitionIndex] with nums1[nums1LeftPartitionIndex +1]. Essentially, this means we are
            # comparing the last elements in the left partitions with the first elements of the right partitions in each array.
            # In order for the left partition to be correct as a whole, all its elements need to be smaller or equal to the elements
            # in the right partition. So, we need:
            # nums1[nums1LeftPartitionIndex] <= nums2[nums2LeftPartitionIndex+1]
            # AND
            # nums2[nums2LeftPartitionIndex] <= nums1[nums1LeftPartitionIndex +1]

            if nums1LeftPartitionValue <= nums2RightPartitionValue and nums2LeftPartitionValue <= nums1RightPartitionValue:
                # we found our left partition and depending on whether the total length is odd or even, we return the right element
                if total % 2 == 0:
                    # the total length is even, so we need to take the average between the last element in the left partition and the first
                    # element in the right partition

                    # the last element in the left partition is the largest element between the last elements in each left partition of our 2 arrays
                    lastLeftPartition = max(nums1LeftPartitionValue, nums2LeftPartitionValue)
                    # the first element in the right partition is the smallest element between the first elements in each right partition of our 2 arrays
                    firstRightPartition = min(nums1RightPartitionValue, nums2RightPartitionValue)

                    return (lastLeftPartition + firstRightPartition) / 2
                else:
                    # the total length is odd, so we need to take the first element in the right partition as our median
                    return min(nums1RightPartitionValue, nums2RightPartitionValue)
            else:
                # here we have 2 scenarios
                # nums1[nums1LeftPartitionIndex] > nums2[nums2LeftPartitionIndex+1]
                # OR
                # nums2[nums2LeftPartitionIndex] > nums1[nums1LeftPartitionIndex +1]
                if nums2LeftPartitionValue > nums1RightPartitionValue:
                    # it means that the last element in the left partition of nums2 is bigger than the first element in the right
                    # partition of nums1. Which means we took too many elements from nums2 and we need to take less.
                    # we need to make our binary search over this array on a smaller scope so we need to push back our `r` index
                    r = middle - 1
                else:
                    # nums1[nums1LeftPartitionIndex] > nums2[nums2LeftPartitionIndex+1]
                    # we took too many elements from nums1 which means we need to take more from nums2 and less from nums1
                    # so we need to include in our left partition of nums2 larger elements. So, we change our `l` index
                    # to start at a place where we could find larger elements of nums2.
                    l = middle + 1

            # since our r is decreasing possibly to a point beyond 0 and our l is increasing possibly to a point beyond the length
            # of the array, we need to make sure that our indices are within range. So, we need to go back and edit the code
            # to handle the cases where nums1LeftPartitionIndex or nums2LeftPartitionIndex could be < 0 and nums1LeftPartitionIndex + 1
            # or nums2LeftPartitionIndex + 1 exceed their arrays lengths.


# nums1 = [1, 3]
# nums2 = [2]

# nums1 = [1, 2]
# nums2 = [3, 4]

nums1 = []
nums2 = [1]

print(Solution2().findMedianSortedArrays(nums1, nums2))
