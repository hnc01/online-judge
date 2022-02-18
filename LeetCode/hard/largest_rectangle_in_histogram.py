'''
    https://leetcode.com/problems/largest-rectangle-in-histogram/

    84. Largest Rectangle in Histogram

    Given an array of integers heights representing the histogram's bar height where the
    width of each bar is 1, return the area of the largest rectangle in the histogram.
'''

'''
    Brute force: we consider the area between every pair of bars and keep track of the max
    
    Accepted but Time Limit Exceeded
    
    Time Complexity: O(n^2)
    Space Complexity: O(1)
'''


class Solution:
    def largestRectangleArea(self, heights: [int]) -> int:
        max_area = float('-inf')

        for i in range(0, len(heights)):
            min_height = float('inf')

            for j in range(i, len(heights)):
                min_height = min(min_height, heights[j])

                current_area = (j - i + 1) * min_height

                max_area = max(max_area, current_area)

        return max_area


'''
    Divide and conquer approach:
    Average Case: O(nlogn)
    Worst Case: O(n^2) [in case the array was sorted]
    Space complexity : O(n). Recursion with worst case depth n.
    
    Accepted but also time limit exceeded
'''


class Solution2:
    def largestRectangleAreaHelper(self, heights, s, e):
        if s == e:
            # we are considering only one bar
            return heights[s]
        elif e < s:
            # our indices are out of bounds => no solution here
            return 0
        else:
            # we need to find the minimum height between s and e
            min_bar = float('inf')
            min_bar_index = -1

            for i in range(s, e + 1):
                if heights[i] < min_bar:
                    min_bar = heights[i]
                    min_bar_index = i

            # our 3 cases are:
            # we create the max area out of the shortest bar + widest area
            min_bar_area = min_bar * (e - s + 1)

            # we create the max area to the left of the shortest bar
            left_of_min_bar_area = self.largestRectangleAreaHelper(heights, s, min_bar_index - 1)

            # we create the max area to the right of the shortest bar
            right_of_min_bar_area = self.largestRectangleAreaHelper(heights, min_bar_index + 1, e)

            return max(min_bar_area, left_of_min_bar_area, right_of_min_bar_area)

    def largestRectangleArea(self, heights: [int]) -> int:
        # the largest area will either be largest by width or by height
        # if it's largest by width then the height will be the height of the shortest bar
        # if it's largest by height, then our max area lies just before or just after our shortest bar
        # the max area is the max among the above 3 options
        return self.largestRectangleAreaHelper(heights, 0, len(heights) - 1)


'''
    In this approach, we still adopt a Divide-and-conquer approach but to avoid the worst-case O(n^2)
    we use a SegmentTree to quickly retrieve the minimum height within a given range (O(nlogn)).
    
    By getting the minimum in O(nlogn) time, we can continue with the divide and conquer approach just like Solution2.
    Note that in Solution2 we were getting the minimum height within a range in O(n) time.
    
    Time complexity : O(nlogn). Segment tree takes O(logn) for a total of n times.
    Space complexity : O(n). Space required for Segment Tree.
'''


class Solution3:
    class SegmentTreeNode:
        start = -1
        end = -1
        min = float('inf')

        def __init__(self, start, end):
            self.start = start
            self.end = end

    def buildSegmentTree(self, heights, start, end):
        if end < start:
            return None

        root = self.SegmentTreeNode(start, end)

        if start == end:
            root.min = start

            return root
        else:
            mid = (start + end) // 2

            root.left = self.buildSegmentTree(heights, start, mid)
            root.right = self.buildSegmentTree(heights, mid + 1, end)

            if root.left is not None and root.right is not None:
                if heights[root.left.min] < heights[root.right.min]:
                    root.min = root.left.min
                else:
                    root.min = root.right.min
            elif root.left is not None:
                root.min = root.left.min
            elif root.right is not None:
                root.min = root.right.min

            return root

    def getMinIndex(self, root, heights, start, end):
        if root is None or (end < root.start) or (start > root.end):
            # the root's start and end index don't intersect with given start-end range
            return -1

        if root.start >= start and root.end <= end:
            # our root is within the given range
            # which means that the min at the root is the min we're looking for
            return root.min

        # our root's range is wider than the given range so we need to narrow it down
        # by checking the minimum of the left and right subtrees
        left_min = self.getMinIndex(root.left, heights, start, end)
        right_min = self.getMinIndex(root.right, heights, start, end)

        if left_min == -1:
            return right_min
        elif right_min == -1:
            return left_min
        else:
            if heights[left_min] < heights[right_min]:
                return left_min
            else:
                return right_min

    def calculateMaxArea(self, heights, root, start, end):
        if start > end:
            # our indices are out of bounds so we can't get any area
            return 0
        elif start == end:
            # we are considering only one element
            return heights[start]
        else:
            # we need to get the index of the min element
            min_bar_index = self.getMinIndex(root, heights, start, end)

            # we need to get the area that's left of the min_bar
            left_max_area = self.calculateMaxArea(heights, root, start, min_bar_index - 1)

            # we need to get the area that's right of the min bar
            right_max_area = self.calculateMaxArea(heights, root, min_bar_index + 1, end)

            # the answer is the max between the area made up by the min_bar_index and left_max_area and right_max_area
            return max(heights[min_bar_index] * (end - start + 1), left_max_area, right_max_area)

    def largestRectangleArea(self, heights):
        # if there are no bars then the max area is 0
        if len(heights) == 0:
            return 0

        root = self.buildSegmentTree(heights, 0, len(heights) - 1)

        return self.calculateMaxArea(heights, root, 0, len(heights) - 1)


'''
    We need to notice a pattern. The probable patterns are:
    heights[i] < heights[i+1] => increasing pattern => nothing stopping the heights[i+1] from growing yet and heights[i] can also expand
    heights[i] > heights[i+1] => decreasing pattern => heights[i] is stopped from expanding by heights[i+1] => only heights[i+1] can expand
    heights[i] = heights[i+1] => similar pattern => both heights[i] and heights[i+1] can expand
    
    so the only pattern we can follow is increasing or similar
    so we only pop when we encounter the decreasing pattern => i.e. we can count the decreasing order as part of our max area computation
    
    when we encounter a decreasing pattern, we need to keep popping all the bars in the stack that have height more than the current height
    because the current height stops them from expanding since it's shorter than them. So we keep popping while top of stack's height is > 
    than current height.
    
    After going through all the heights and popping/adding to stack as we go along, we might end up with elements in the stack at the end.
    The elements that stay in the stack at the end are the elements that can expand all the way to the end of the histogram. So, their width
    is computed with respect to their index AND len(heights).
    
    Explanation: https://www.youtube.com/watch?v=zx5Sw9130L0
    
    Accepted:
    Time complexity : O(n). nn numbers are pushed and popped.
    Space complexity : O(n). Stack is used.
'''


class Solution4:
    def largestRectangleArea(self, heights):
        # we will use this to help us with our algorithm
        # this will contain (index, height) where height is the height of a bar
        # and index is the leftmost index where this particular height can be expanded.
        stack = []

        # this will help us keep track of the max area across the histogram
        max_area = float('-inf')

        for i in range(0, len(heights)):
            left_most_index = -1

            while len(stack) > 0 and stack[len(stack) - 1][1] > heights[i]:
                # while the top of the stack is height that is greater than current height
                # we need to pop that height because it can't expand further
                top_index, top_height = stack.pop()

                # width of top_height is the distance between its starting index and the current index i
                # because it can't expand left past its starting index and it can't expand right past i
                current_area = (i - top_index) * top_height

                max_area = max(max_area, current_area)

                left_most_index = top_index

            # left_most_index marks the left boundary of current height (i.e. the farthest index to which
            # the current height can expand to the left)
            if left_most_index == -1:
                stack.append((i, heights[i]))
            else:
                stack.append((left_most_index, heights[i]))

        # now we need to pop the remaining elements in the stack
        while len(stack) > 0:
            # this bar can expand from top_index all the way to the right
            # so its width is len(heights) - top_index
            top_index, top_height = stack.pop()

            current_area = (len(heights) - top_index) * top_height

            max_area = max(max_area, current_area)

        return max_area


heights = [2, 1, 5, 6, 2, 3]
# heights = [2, 4]
print(Solution4().largestRectangleArea(heights))
