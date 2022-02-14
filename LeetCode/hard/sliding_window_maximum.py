'''
    https://leetcode.com/problems/sliding-window-maximum/

    239. Sliding Window Maximum

    You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of
    the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

    Return the max sliding window.
'''

'''
    Accepted but Time Limit Exceeded
    
    The bottleneck is the fact that we need to iterate over the window if
    prev_max > nums[end]
    
    The below is O(n^2) (enhanced brute force but still not good enough)
'''


class Solution:
    def maxSlidingWindow(self, nums: [int], k: int) -> [int]:
        # the length of nums
        n = len(nums)

        if k > n:
            return [0]
        else:
            max_sliding_window = []

            # the window starts here
            start = 0
            # the window ends here
            end = k - 1

            # this will help us keep track of the max number
            prev_max = max(nums[start:k])

            max_sliding_window.append(prev_max)

            while start < n and end < n:
                start += 1
                end += 1

                if end < n:
                    if nums[end] >= prev_max:
                        prev_max = nums[end]
                    else:
                        # we need to iterate between start and end-1 to find the max of the window
                        prev_max = max(nums[start:end + 1])

                    max_sliding_window.append(prev_max)

            return max_sliding_window


'''
    Accepted
    
    We create a double sided queue so we can easily remove from beginning and end of the queue.
    The idea here is that we update the queue such that the leftmost element is always the largest element.
    Since we update the queue with every new element added, we're sure that the leftmost element in the queue
    is also the largest for current window.
    Whenever the window boundaries change, we make sure that the elements in the queue are also within boundaries
    so we remove from the left side all the elements that have index < start. By popping from the queue all elements
    less than current new element (nums[end]), we're making sure that the elements in the queue are stored in decreasing
    order from left to right.
'''
from collections import deque


class Solution2:
    def maxSlidingWindow(self, nums: [int], k: int) -> [int]:
        # the length of nums
        n = len(nums)

        if k > n:
            return [0]
        else:
            max_sliding_window = []

            queue = deque()

            # the window starts here
            start = 0
            # the window ends here
            end = k - 1

            # first we will add all the elements from start to end to the queue
            current_max = float('-inf')

            for i in range(start, end + 1):
                # while the current element is larger than the last element in the queue,
                # we will keep emptying the queue
                while len(queue) > 0 and queue[len(queue) - 1][0] <= nums[i]:
                    queue.pop()

                # now we're sure that we removed all the elements <= to current number
                # until either the queue is empty or we reached an element greater than current
                # in the queue we will append elements along with their index to make sure
                # that the queue always contains elements in the current active window
                queue.append((nums[i], i))

                current_max = max(current_max, nums[i])

            # we append the max of current window too the max_sliding_window
            max_sliding_window.append(current_max)

            # now we will move the window one element to the right in each iteration and see what we get
            while start < n and end < n:
                start += 1
                end += 1

                if end < n:
                    # we need to check if the first element in the queue is still within range
                    if queue[0][1] < start:
                        # if it's not in range then we need to remove it and not take it into consideration
                        queue.popleft()

                    # then we need to keep popping from the queue until the queue is empty OR we find an element
                    # greater than current element
                    while len(queue) > 0 and queue[len(queue) - 1][0] <= nums[end]:
                        queue.pop()

                    queue.append((nums[end], end))

                    max_sliding_window.append(queue[0][0])

            return max_sliding_window


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

# nums = [1,6,-1,3,2,1,6,7,5,4,9,-2,-1]
# k = 4

# nums = [1]
# k = 1

# nums = []
# k = 2

# nums = [1, -1]
# k = 1

print(Solution2().maxSlidingWindow(nums, k))
