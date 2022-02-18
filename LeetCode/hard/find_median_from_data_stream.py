'''
    https://leetcode.com/problems/find-median-from-data-stream/

    295. Find Median from Data Stream

    The median is the middle value in an ordered integer list. If the size of the list is even, there is no
    middle value and the median is the mean of the two middle values.
        - For example, for arr = [2,3,4], the median is 3.
        - For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

    Implement the MedianFinder class:
        - MedianFinder() initializes the MedianFinder object.
        - void addNum(int num) adds the integer num from the data stream to the data structure.
        - double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
'''

'''
    Accepted
    
    Similar to Approach 2 in the list of Leetcode solutions
'''


class MedianFinder:
    values = None

    def __init__(self):
        self.values = []

    def addNum(self, num: int) -> None:
        if len(self.values) == 0:
            self.values.append(num)
        else:
            # we need to find the place of num by doing binary search
            index = self.binarySearch(0, len(self.values) - 1, num)

            self.values.insert(index, num)

    def binarySearch(self, start, end, key):
        if end <= start:
            # if the value is here then we returned the right index
            # if the value is not here then we returned the index where it should be inserted
            if key < self.values[start]:
                return start
            else:
                return start + 1
        else:
            mid = (start + end) // 2

            if self.values[mid] == key:
                return mid
            elif key < self.values[mid]:
                # key is in the left side of the array
                return self.binarySearch(start, mid - 1, key)
            else:
                return self.binarySearch(mid + 1, end, key)

    def findMedian(self) -> float:
        # if the number of elements is odd then the median is the middle element
        if len(self.values) % 2 == 1:
            return self.values[len(self.values) // 2]
        else:
            # it's the mean of the 2 middle elements
            left_element = self.values[(len(self.values) // 2) - 1]
            right_element = self.values[len(self.values) // 2]

            return (left_element + right_element) / 2


'''
    In the above solution, every time we do addNum, we need O(logn) to find the index and then O(n) to place num in the values array.
    Then, finding the median is O(1) because we simply do a quick calculation based on whether the array is even or odd.
    
    For addNum, the complexity is O(logn) + O(n) ~= O(n)
    
    To improve the above, we need another data structure such that inserting an element doesn't require O(n). Since we don't need all the elements
    sorted to get the median [explanation: we only need the left median and right median to be in place], we can maintain 2 heaps where one heap
    contains the lower half of the array (all the elements less than the median) and one heap contains the upper half of the array (all the elements
    more than the median).
    
    In the first heap, we need quick access to the left median => largest number in the left half of the array => max heap (low)
    In the second heap, we need quick access to the right median => smallest number in the right half of the array => min heap (high)
    
    The nb of elements can be odd => in which case we'll allow `low` to contain the 1 extra element => len(low) = n + 1 and len(high) = n
    The nb of elements can be even => in which case both heaps `low` and `high` contain n elements.
    
    Accepted
'''
import heapq


class MedianFinder2:
    low = None
    high = None

    def __init__(self):
        self.low = []
        self.high = []

    def addNum(self, num: int) -> None:
        '''
            We directly add `num` to low.

            Since num might actually belong to the upper half (i.e., high), we balance
            high and low by removing the max of low and putting it in high.

            By removing from low and adding to high, we might end up breaking the property that
            high and low must be both n or that low is n+1 and high is n.

            So, to make sure that we don't break the number of elements property, we check if the
            length of low is now less than high, if it is, we remove an `extra` element from high
            (we choose the min in high) and put it in low.
        '''
        # directly add num to low
        heapq.heappush(self.low, -1 * num)  # to get low to act like a max heap, we need to insert in it neg elements

        # since we added a new element to low, we need to add the largest element in low to high
        # to keep both trees balanced (size n for high and size n or n+1 for low)
        heapq.heappush(self.high, heapq.heappop(self.low) * -1)

        # now we check how many elements are in `high` compared to `low`
        if len(self.high) > len(self.low):
            heapq.heappush(self.low, heapq.heappop(self.high) * -1)

    def findMedian(self) -> float:
        # if both heaps have same length then we have an even number of elements
        # so the median is the mean of the max of low and min high
        if len(self.low) == len(self.high):
            return ((self.low[0] * -1) + self.high[0]) / 2
        else:
            # the number of elements odd and the middle element is the max of `low`
            # since `low` is allowed to hold n+1 elements in such cases
            return (self.low[0] * -1)


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder2()
obj.addNum(2)
obj.addNum(4)
obj.addNum(3)
obj.addNum(1)
obj.addNum(5)
obj.addNum(2)

param_2 = obj.findMedian()

print(param_2)
