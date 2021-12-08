'''
    https://leetcode.com/problems/combination-sum/

    Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

    The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

    It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
'''

'''
    Accepted
'''

class Solution:
    def combination_sum_helper(self, candidates, target, index, current_result, results):
        current_result_sum = sum(current_result)

        if current_result_sum == target:
            results.append(current_result)
        elif current_result_sum < target:
            if index < len(candidates):
                # we have 2 options:
                # we add the same element again
                current_result_1 = current_result.copy()
                current_result_1.append(candidates[index])

                self.combination_sum_helper(candidates, target, index, current_result_1, results)

                # we move on to other elements after it
                # we need to check combinations of current element with each one after it in the list
                # and not just the one immediately after it
                for j in range(index+1, len(candidates)):
                    current_result_2 = current_result.copy()
                    current_result_2.append(candidates[j])

                    self.combination_sum_helper(candidates, target, j, current_result_2, results)

    def combinationSum(self, candidates: [int], target: int) -> [[int]]:
        candidates.sort()

        combinations = []

        for i in range(0, len(candidates)):
            if candidates[i] <= target:
                if candidates[i] == target:
                    combinations.append([candidates[i]])
                else:
                    # candidates[i] < target
                    current_results = []

                    self.combination_sum_helper(candidates, target, i, [candidates[i]], current_results)

                    combinations = combinations + current_results

        return combinations


print(Solution().combinationSum([1], 2))