'''
    https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/

    1477. Find Two Non-overlapping Sub-arrays Each With Target Sum

    You are given an array of integers arr and an integer target.

    You have to find two non-overlapping sub-arrays of arr each with a sum equal target.
    There can be multiple answers so you have to find an answer where the sum of the lengths of the two sub-arrays is minimum.

    Return the minimum sum of the lengths of the two required sub-arrays, or return -1 if you cannot find such two sub-arrays.
'''
import math

'''
    The solution is correct but takes too much time. The recursion overhead is too much and is causing stackoverflow.
    
    Need to create an interative solution.
'''


class Solution:
    def generateSubArrays(self, s, size, arr, target, subarrays):
        # we going into the recursion until we reach the end of the array i.e. the start of the subarray and its size exceed array length
        if (s + size) <= len(arr):
            # at each step we either continue with the next element in the array or we stop and start a new subarray
            if sum(arr[s:s + size]) == target:
                # add it to our list of possible solutions
                # we add the start and end indices of the subarray
                subarrays.add((s, s + size))

                # move on by starting with a new subarray at current position e because we have 2 cases:
                # - we either keep adding 0s => this will keep subarray sum = target but won't lead to solution with min length => not valid
                # - we keep adding elements => this will make our sum > target because all the elements > 0 => not valid
            elif sum(arr[s:s + size]) < target:
                # here we need to explore both options: keep moving forward with size + 1 AND starting a new subarray at s + size

                # moving forward with size + 1
                self.generateSubArrays(s, size + 1, arr, target, subarrays)

            # elif sum(arr[s:s + size]) > target:
            # our only option is to ditch the subarray we current have and start a new one starting at s + size

            # now matter in which case we are, we always need to explore the option of starting a new subarray so we put it here after all the ifs
            self.generateSubArrays(s + size, 1, arr, target, subarrays)

    def minSumOfLengths(self, arr: [int], target: int) -> int:
        # first, we get all subarrays that sum up to target
        subarrays = set()

        self.generateSubArrays(0, 1, arr, target, subarrays)

        if len(subarrays) <= 1:
            # we either found no subarrays or we found only one. Either way, we don't have enough to return a valid solution
            return -1
        else:
            subarrays = list(subarrays)

            min_length = float('inf')

            # we have more than one subarray to consider so we need to find all non-overlapping pairs
            for i in range(0, len(subarrays)):
                first_subarray = subarrays[i]

                for j in range(i + 1, len(subarrays)):
                    second_subarray = subarrays[j]

                    # they are overlapping if one starts after the other is done
                    if (first_subarray[1] <= second_subarray[0]) or (second_subarray[1] <= first_subarray[0]):
                        # they are non-overlapping
                        min_length = min(min_length, (first_subarray[1] - first_subarray[0]) + (second_subarray[1] - second_subarray[0]))

            if math.isinf(min_length):
                return -1

            return min_length


'''
    Time limit exceeded still!
'''


class Solution2:
    def minSumOfLengths(self, arr: [int], target: int) -> int:
        solutions = []

        i = 0

        while i < len(arr):
            do_increment = True

            for j in range(i, len(arr)):
                if sum(arr[i:j + 1]) == target:
                    solutions.append((i, j))

                    # since we already found a solution starting at i
                    # there's no way to find another one with shorter length => break
                    break
                elif arr[j] > target:
                    # if the current element we're trying to add is > target and we haven't found our solution yet
                    # then there's no solution starting with i we need to move it past j
                    i = j + 1

                    do_increment = False

                    break
                elif sum(arr[i:j + 1]) > target:
                    # we couldn't find a solution starting at i and we already exceeded the target
                    break

            if do_increment:
                i += 1

        if len(solutions) <= 1:
            # we either found no subarrays or we found only one. Either way, we don't have enough to return a valid solution
            return -1
        else:
            min_length = float('inf')

            # we have more than one subarray to consider so we need to find all non-overlapping pairs
            for i in range(0, len(solutions)):
                first_subarray = solutions[i]
                first_subarray_length = first_subarray[1] - first_subarray[0] + 1

                if first_subarray_length < min_length:
                    for j in range(i + 1, len(solutions)):
                        second_subarray = solutions[j]
                        second_subarray_length = second_subarray[1] - second_subarray[0] + 1

                        if second_subarray_length < min_length:
                            # they are overlapping if one starts after the other is done
                            if (first_subarray[1] < second_subarray[0]) or (second_subarray[1] < first_subarray[0]):
                                # they are non-overlapping
                                min_length = min(min_length, first_subarray_length + second_subarray_length)

            if math.isinf(min_length):
                return -1

            return min_length


'''
    Try a sliding window solution to gather all the subarrays with sum target
'''


class Solution3:
    def minSumOfLengths(self, arr: [int], target: int) -> int:
        solutions = []

        # the start and end of current subarray
        s = e = 0

        while s < len(arr) and e < len(arr):
            if sum(arr[s:e + 1]) == target:
                # we found a subarray from s to e st sum is target
                # we add it to solutions and we increments both s and e by 1 to slide the window
                solutions.append((s, e))

                s += 1
                e += 1
            elif sum(arr[s:e + 1]) < target:
                # we need to keep expanding the window to the right
                e += 1
            elif sum(arr[s:e + 1]) > target:
                # we exceeded our sum and couldn't find a solution for subarray starting at s
                # so we start the window at s += 1 => keep removing elements from the left to reduce window sum
                s += 1

                if s > e:
                    e = s  # we reset the window

        if len(solutions) <= 1:
            # we either found no subarrays or we found only one. Either way, we don't have enough to return a valid solution
            return -1
        else:
            min_length = float('inf')

            # we have more than one subarray to consider so we need to find all non-overlapping pairs
            for i in range(0, len(solutions)):
                first_subarray_length = solutions[i][1] - solutions[i][0] + 1

                if first_subarray_length < min_length:
                    for j in range(i + 1, len(solutions)):
                        second_subarray_length = solutions[j][1] - solutions[j][0] + 1

                        if second_subarray_length < min_length:
                            # they are overlapping if one starts after the other is done
                            if (solutions[i][1] < solutions[j][0]) or (solutions[j][1] < solutions[i][0]):
                                # they are non-overlapping
                                min_length = min(min_length, first_subarray_length + second_subarray_length)

            if math.isinf(min_length):
                return -1

            return min_length


'''
    Now the problem is checking all the subarrays to see the non-overlapping ones and find min lengths.
    We need to slowly build towards our solution while we're gathering the subarrays that sum up to target.
    
    Way better performance but still time limit exceeded.
'''


class Solution4:
    def minSumOfLengths(self, arr: [int], target: int) -> int:
        # non-overlapping arrays mean that one ends before the other starts
        # this means that first[end] < second[start]
        # if we have the min-length array with sum target up to `end` then we can safely test it
        # against our current subarray if our subarray starts AFTER `end`

        # the start and end of current subarray
        s = e = 0

        # min_length_so_far[i] => the length of the smallest array with sum = target between [0 and i]
        # by default, the min_length of array between 0 and i is max int so we can safely to min(a,b) and override this default value
        min_length_so_far = [float('inf')] * len(arr)
        overall_min_length = float('inf')

        # we need to explore e at every stop so we can't increment it within the loop. Only at the end we increment by 1.
        while s < len(arr) and e < len(arr):
            # while we are in a subarray that has sum > target, we need to keep reducing our window size to finally reach a
            # subarray with sum <= target => while keeping same end index `e`. If we increase the window size from the right,
            # we'd be possibly losing a solution that ends at `e`.
            while sum(arr[s:e + 1]) > target:
                # this loop is the only place we update the s pointer
                s += 1

            # when we exit this it would either mean: (1) we reached a subarray whose sum <= target or (2) we reached an empty array with sum 0

            if sum(arr[s:e + 1]) == target:
                # we found a subarray from s to e st sum is target
                # we add it to solutions and we increments both s and e by 1 to slide the window

                # now that we found a new array with target sum, we need to if its length along with smallest before it
                # if we get a better min_length
                # the new min_length is either the existing min_length we have so far OR the new solution

                # update the overall min length seen so far
                overall_min_length = min(overall_min_length, min_length_so_far[s - 1] + (e - s + 1))
                # update the min_length seen so far at e by comparing it with the min_length at e-1
                # the below array has nothing to do with the overall returned solution. this just keeps track of subarrays with sum target
                # that are of minimum length seen so far (i.e., up to index e)
                min_length_so_far[e] = min(min_length_so_far[e - 1], (e - s + 1))
            elif sum(arr[s:e + 1]) < target:
                # this means that we don't have any target subarrays that end at e so the solution at e is same as solution
                # ending at e-1
                min_length_so_far[e] = min_length_so_far[e - 1]

                # we need to keep expanding the window to the right => which will be done by default at the end of the loop

            e += 1

        if math.isinf(overall_min_length):
            return -1
        else:
            return overall_min_length


'''
    Same as above, but instead computing the sum of the subarray at each if, we compute the sum incrementally and save it in
    current subarray sum.
    
    This change made it Accepted.
    
    Summary:
    - We need to keep track of the min lengths seen so far on the fly while computing the subarray solutions (DP)
    - We need to keep track of the sum of the current subarray in a variable instead of recomputing with every loop iteration.
'''


class Solution5:
    def minSumOfLengths(self, arr: [int], target: int) -> int:
        # non-overlapping arrays mean that one ends before the other starts
        # this means that first[end] < second[start]
        # if we have the min-length array with sum target up to `end` then we can safely test it
        # against our current subarray if our subarray starts AFTER `end`

        # the start and end of current subarray
        s = e = current_subarray_sum = 0

        # min_length_so_far[i] => the length of the smallest array with sum = target between [0 and i]
        # by default, the min_length of array between 0 and i is max int so we can safely to min(a,b) and override this default value
        min_length_so_far = [float('inf')] * len(arr)
        overall_min_length = float('inf')

        # we need to explore e at every stop so we can't increment it within the loop. Only at the end we increment by 1.
        while s < len(arr) and e < len(arr):
            current_subarray_sum += arr[e]

            # while we are in a subarray that has sum > target, we need to keep reducing our window size to finally reach a
            # subarray with sum <= target => while keeping same end index `e`. If we increase the window size from the right,
            # we'd be possibly losing a solution that ends at `e`.
            while current_subarray_sum > target:
                current_subarray_sum -= arr[s]

                # this loop is the only place we update the s pointer
                s += 1

            # when we exit this it would either mean: (1) we reached a subarray whose sum <= target or (2) we reached an empty array with sum 0

            if current_subarray_sum == target:
                # we found a subarray from s to e st sum is target
                # we add it to solutions and we increments both s and e by 1 to slide the window

                # now that we found a new array with target sum, we need to if its length along with smallest before it
                # if we get a better min_length
                # the new min_length is either the existing min_length we have so far OR the new solution

                # update the overall min length seen so far
                overall_min_length = min(overall_min_length, min_length_so_far[s - 1] + (e - s + 1))
                # update the min_length seen so far at e by comparing it with the min_length at e-1
                # the below array has nothing to do with the overall returned solution. this just keeps track of subarrays with sum target
                # that are of minimum length seen so far (i.e., up to index e)
                min_length_so_far[e] = min(min_length_so_far[e - 1], (e - s + 1))
            elif current_subarray_sum < target:
                # this means that we don't have any target subarrays that end at e so the solution at e is same as solution
                # ending at e-1
                min_length_so_far[e] = min_length_so_far[e - 1]

                # we need to keep expanding the window to the right => which will be done by default at the end of the loop

            e += 1

        if math.isinf(overall_min_length):
            return -1
        else:
            return overall_min_length


print(Solution5().minSumOfLengths(arr=[3, 2, 2, 4, 3], target=3))
# print(Solution4().minSumOfLengths(arr=[7, 3, 4, 7], target=7))
print(Solution5().minSumOfLengths(arr=[4, 3, 2, 6, 2, 3, 4], target=6))
# print(Solution2().minSumOfLengths([1, 1, 1, 2, 2, 2, 4, 4], 6))
# print(Solution4().minSumOfLengths([2,2,4,4,4,4,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 20))
# print(Solution5().minSumOfLengths([2, 2, 4, 4, 4, 4, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 20))
