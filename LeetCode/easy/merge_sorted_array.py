class Solution:
    def merge(self, nums1: [int], m: int, nums2: [int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j, r = 0, 0, 0

        while i < m and j < n:
            if nums2[j] <= nums1[r]:
                # insert nums2[j] at i in nums[1]
                # we shift to the right all the elements in nums1 from i to n + m
                carryElement = nums1[r]

                for k in range(r + 1, n + m):
                    carryElement, nums1[k] = nums1[k], carryElement

                nums1[r] = nums2[j]
                j += 1
                r += 1
            else:
                # nums2[j] > nums1[i]
                i += 1
                r += 1

        # we might still have elements in nums2 that we didn’t take care of
        while r < n + m and j < n:
            nums1[r] = nums2[j]
            j += 1
            r += 1
