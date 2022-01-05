'''
    https://leetcode.com/problems/find-the-duplicate-number/

    287. Find the Duplicate Number

    Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

    There is only one repeated number in nums, return this repeated number.

    You must solve the problem without modifying the array nums and uses only constant extra space.
'''

'''
    This would work if the problem specified that the repeated element would be repeated exactly once
'''


class Solution:
    def findDuplicate(self, nums: [int]) -> int:
        repeated_number = nums[0]

        # here we obtain the XOR of all of them together so here the duplicate element would be eliminated from the total
        # so if we have 1,3,4,2,2 then the XOR product would be just 1^3^4
        for i in range(1, len(nums)):
            repeated_number ^= nums[i]

        # then we list all the elements that would be in original array without repetition: 1,2,3,4
        # then we XOR [1,2,3,4] with [1,3,4] (product we got earlier). From this it's clear that 1 will cancel 1, 3 will cancel 3 and 4 will cancel 4
        # the only element that will remain is the one that eliminated while building the product which is the repeated element which is in this case 2
        for i in range(1, len(nums)):
            repeated_number ^= i

        return repeated_number


'''
    Approach 3: Negative Marking [Accepted]
    
    The idea behind this is that we use the values in the array as indexes within the array. Everytime we see an element, we mark array[element] by
    flipping its sign. So, when array[element] is < 0 it means we've already seen `element`. So, while traversing the array, if we check array[element]
    and we saw that it's already negative, it means we passed through `element` before and so it's a duplicate.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
'''


class Solution2:
    def findDuplicate(self, nums: [int]) -> int:
        for i in range(0, len(nums)):
            current_index = abs(nums[i])

            if nums[current_index] < 0:
                # we already marked this cell which means we've seen its index before
                return current_index
            else:
                nums[current_index] *= -1


'''
    Approach 4.1: Array as HashMap (Recursion) [Accepted]
    
    Instead of flipping the sign of each array[element], we store element at array[element] for each element. We backup the old value at array[element]
    and we try to place it in the next recursive call. When we encounter a case where array[element] is already equal to element. It means we have a duplicate.
    Note that in this solution, since no element will be mapped to index 0 since all elements are in [1,n], nums[0] can be set to 0.
    
    
    Time Complexity: O(n)
    Space Complexity: O(n) [because of the recursion stack]
'''


class Solution3:
    def find_duplicate_helper(self, nums, current_element):
        if nums[current_element] == current_element:
            return current_element
        else:
            next_element = nums[current_element]
            nums[current_element] = current_element

            return self.find_duplicate_helper(nums, next_element)

    def findDuplicate(self, nums: [int]) -> int:
        return self.find_duplicate_helper(nums, 0)


'''
    Approach 4.2: Array as HashMap (Iterative) [Accepted]
    Same as above but iterative.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
'''


class Solution4:
    def findDuplicate(self, nums: [int]) -> int:
        current_element = 0

        while True:
            if nums[current_element] == current_element:
                break
            else:
                next_element = nums[current_element]
                nums[current_element] = current_element
                current_element = next_element

        return current_element


'''
    Approach 5: Binary Search [Accepted]
    The idea here is that we check at each iteration the 'mid' element. If the mid element's count (i.e. number of elements less than or equal to it) 
    is less than or equal to it, then it means that the mid element along with all the numbers before it don't have any duplicates because their counts
    are correct. Why? because the numbers are from [1,n] so for number 4 for example, we know that the number of elements less than or equal to it is at
    more 4 [1,2,3,4] (some numbers might be missing that's why we need the `less than`). In this case, we move our attention to the right section and repeat.
    If the mid element's count is not correct, then we need to repeat the search on the right section because the incorrect count propagates from a number to
    all the numbers greater than it. So, if at mind we have a wrong count, then it either originated at mid OR somewhere before it.
    
    We return the smallest mid where the count is wrong.
    
    Time Complexity: O(n log n)
    Space Complexity: O(1)
'''


class Solution5:
    def findDuplicate(self, nums: [int]) -> int:
        # Note: we use the indices from [1,n] to mimic that we're checking each number from 1 to n to see how many times
        # they appear in the array. We don't check the counts of numbers by pulling the numbers from the nums in the array
        # because sometimes the array contains only the duplicate number [2,2,2,2,2]
        # Also, the reason we use the indices is to make sure that our count array looks like this (1,2,3,4,5,6)
        # if we use the values in the array, then if the array is [1,2,5,3] the count will be (1,2,4,3) which is not in ascending order
        # and so we can't use binary sort on such a count array.

        # the start and end  of the current section of the array we're exploring
        start = 0
        end = len(nums) - 1

        duplicate = -1

        while start <= end:
            # calculate the mid element
            # at index mid, we need to have in the array at most mid element less than or equal to mid
            mid = int((start + end) / 2)

            # get the count of the number of elements less than or equal to nums[mid]
            mid_count = sum(num <= mid for num in nums)

            if mid_count <= mid:
                # it means that the count at mid is correct so we need to explore the section after it
                start = mid + 1  # we need to skip the entire mid index because we already checked its count
            else:
                # it means that the count at mid is not correct so we need to explore the section before it
                duplicate = mid
                end = mid - 1  # we need to skip the entire mid index because we already checked its count

        return duplicate


'''
    Approach 7: Floyd's Tortoise and Hare (Cycle Detection) [Accepted]
    
    This is an approach to detect cycles in linked lists and can be used to solve 'linked_list_cycle_ii.py'
    
    The idea is that we split the solution into 2 phases and utilize 2 pointers: tortoise and hare. Tortoise moves one step at a time if the tortoise
    is at index i, then its next position is at nums[i]. Hare moves twice as fast as in if the hare is at index i, then its next position is nums[nums[i]].
    
    Since the hare moves twice as fast as tortoise, after some time, they will meet a certain intersection point. After they meet, we say that the tortoise lost this race.
    
    Now phase 2 comes in. We give the tortoise another chance by putting it at the start again AND by slowing down the hare. So now, if tortoise is at 
    index i then its next position is nums[i]; same for the hare. According to a mathematical equation, it will take the tortoise F jumps to go from 0 to point F (start of the cycle)
    and it will take the hare F jumps to move through the cycle and reach the point F (start of the cycle). So, when the hare and tortoise meet in phase 2, this would
    be the point where the cycle starts. Since the cycle is present in the linked list because there are duplicates, the point where the tortoise and hare
    meet in phase 2 is actually the entrance to the cycle and is the element that is a duplicate in the list.
    
    Time Complexity: O(n)

    Space Complexity: O(1)
'''


class Solution6:
    def findDuplicate(self, nums: [int]) -> int:
        # both pointers start at the beginning
        tortoise = 0
        hare = 0

        # PHASE 1
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]

            if tortoise == hare:
                break

        # PHASE 2
        # we put the tortoise at the beginning
        tortoise = 0

        # we keep the hare in the same position where the previous phase ended
        while True:
            tortoise = nums[tortoise]
            hare = nums[hare]

            if tortoise == hare:
                break

        # here tortoise = hare = element entrance of cycle
        # we can return either tortoise or hare
        return tortoise


# nums = [3, 1, 4, 3, 2]
nums = [1, 2, 4, 3, 2]

print(Solution6().findDuplicate(nums))
