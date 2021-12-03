'''
    Brute Force Approach
'''


class Solution:
    def maxArea(self, height) -> int:
        max_area = 0

        for i in range(0, len(height)):
            for j in range(i + 1, len(height)):
                # area is width x length
                # width is always j - i
                w = j - i

                # height is the min between list[i] and list[j]
                h = min(height[i], height[j])

                if w * h > max_area:
                    max_area = w * h

        return max_area


class Solution2:
    '''
        Idea: we need to maximum area and to maximize are we need to maximum height and width of the container

        Observations:
        - the further the lines are from each other the higher the width
        - the height of the container is always bound by the shortest line (height)

        Key ideas:
        - if we're examining 2 lines and the left line is shorter, then the only thing we can do to increase area is
        to move the pointer of the left line closer to the right. That way we might find a taller line to compensate for
        the loss in width. But, we can't move the right line more to the left because that will for sure decrease the area
        since the height would still be bound by the left line (which is shorter) and by moving the right line to the left
        we'd be decreasing the width
        - same observation but in reverse in case the right line was shorter than the left line

    '''
    def maxArea(self, height) -> int:
        max_area = 0

        left_pointer = 0
        right_pointer = len(height) - 1

        while left_pointer < right_pointer:
            w = right_pointer - left_pointer
            h = min(height[left_pointer], height[right_pointer])

            current_area = w * h

            if current_area > max_area:
                max_area = current_area

            if height[left_pointer] < height[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1

        return max_area


print(Solution2().maxArea([4, 3, 2, 1, 4]))
