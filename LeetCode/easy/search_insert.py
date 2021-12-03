def searchInsert(nums: list, target: int) -> int:
    start_index = 0  # first index in array
    end_index = len(nums) - 1  # last index in array

    # as long as start_index is not equal to end_index and it's still less than it
    # then it means we can keep searching
    while start_index < end_index:
        mid_index = int(start_index + (end_index - start_index) / 2)

        if nums[mid_index] == target:
            return mid_index
        elif target <= nums[mid_index]:
            # target must be in left side of array
            end_index = mid_index - 1 # we need to skip the pivot because we already checked it
        else:
            # target must be in right side of array
            start_index = mid_index + 1 # we need to skip the pivot because we already checked it

    # at the end of the while loop, we reach the single position in
    # the array where target should be OR where it is (start_index = end_index)
    if nums[start_index] < target:
        return start_index + 1
    else:
        return start_index


print(searchInsert([1, 3, 5, 6], 0))
