'''
    Solution 1: Brute Force: Time Limit Exceeded
'''


class Solution:
    def combinations_helper(self, arr, n, r, index, data, i, result):
        # arr[] ---> Input Array
        # data[] ---> Temporary array to store current combination
        # start & end ---> Starting and Ending indexes in arr[]
        # index ---> Current index in data[]
        # r ---> Size of a combination to be printed

        if (index == r):
            # Current combination is done (it's the proper size)
            temp = ()

            for j in range(r):
                temp = temp + (data[j],)

            result.append(tuple(sorted(temp)))

            return

        if (i >= n):
            # When no more elements are there to put in data[]
            return

        # current is included, put next at next location
        data[index] = arr[i]

        self.combinations_helper(arr, n, r, index + 1, data, i + 1, result)

        # current is excluded, replace it with next (Note that i+1 is passed, but index is not changed)
        self.combinations_helper(arr, n, r, index, data, i + 1, result)

    def generate_combinations(self, arr, n, r):
        data = list(range(r))

        result = []

        self.combinations_helper(arr, n, r, 0, data, 0, result)

        return result

    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        else:
            result = set()

            combinations_of_3 = self.generate_combinations(nums, len(nums), 3)

            for combination in combinations_of_3:
                if sum(list(combination)) == 0:
                    result.add(combination)

            return [list(x) for x in result]

'''
    Solution 2 [Accepted]: reduced the problem to sum of 2 by doing a loop and fixing each time one of the digits as a pivot
    The sums between each 2 digits is calculated in advance using create_sums_matrix. To reduce computation, we calculate only
    one part of the matrix (everything above diagonal) because matrix is symmetrical.
    Since we're always looking for pairs that have a certain sum and not the other way around, we map sums to lists of pairs.
    Also, to eliminate unnecessary computations in case of duplicates in the array, we make sure that we don't process the same
    value for a pivot more than once by saving the processed pivot values in a set.
'''
class Solution2:
    def create_sums_matrix(self, nums):
        memo_sums = {}

        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                # we don't care about the diagonal sum in the matrix so we start with i+1
                sum = nums[i] + nums[j]

                if sum not in memo_sums:
                    memo_sums[sum] = []

                memo_sums[sum].append((i, j))

        return memo_sums

    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        else:
            memo_sums = self.create_sums_matrix(nums)

            # these are the values we've already calculated results for as pivots (ie first element we choose)
            # if we have duplicates in the array, then we won't explore the solutions for the same pivot elements
            # because they would all be same solutions
            pivot_values = set()

            results = set()

            for x in range(0, len(nums)):
                if nums[x] not in pivot_values:
                    pivot_values.add(nums[x])

                    # sum left = nums[x] + y + z = 0 => y + z = -nums[x]
                    new_sum = -nums[x]

                    # get all the indices that have the sum new_sum
                    if new_sum in memo_sums:
                        # it means we can sum x with another 2 elements to get 0
                        candidates = memo_sums[new_sum]

                        for (y, z) in candidates:
                            if y != x and z != x:
                                temp = [nums[x], nums[y], nums[z]]

                                results.add(tuple(sorted(temp)))

                    # else: we can't sum x with anything that produces 0 so we pass on it

            return [list(h) for h in results]



print(Solution2().threeSum([1,1,0]))
