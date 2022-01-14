'''
    https://leetcode.com/problems/daily-temperatures/

    739. Daily Temperatures

    Given an array of integers temperatures represents the daily temperatures, return an array answer such
    that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.
    If there is no future day for which this is possible, keep answer[i] == 0 instead.
'''

'''
    Correct but time limit exceeded.
'''


class Solution:
    def dailyTemperatures(self, temperatures: [int]) -> [int]:
        if len(temperatures) <= 0:
            return []

        answers = [0] * len(temperatures)

        # this dict will map every number we see in temperatures to its list of indices
        temperatures_indices = {}

        # since we wont be passing through temperatures[len(temperatures)-1] in the below loop
        # we need to add the last temp to the counts of temperatures
        temperatures_indices[temperatures[len(temperatures) - 1]] = []
        temperatures_indices[temperatures[len(temperatures) - 1]].append(len(temperatures) - 1)

        # we loop over the temperatures array backwards because for a given temperatures at i,
        # we only care about the temperatures after it. Also, the only answer we know upfront is that
        # answers[len(temperatures)-1] is always 0.
        for i in range(len(temperatures) - 2, -1, -1):
            current_temp = temperatures[i]

            if current_temp not in temperatures_indices:
                temperatures_indices[current_temp] = []

            temperatures_indices[current_temp].append(i)

            # the values that could be greater than current_temp and in the array
            # are from current_temp + 1 to 100. So we loop over that range to see
            # if any of these values is present in the array after current_temp
            for t in range(current_temp + 1, 101):
                if t in temperatures_indices:
                    closest_index = temperatures_indices[t][len(temperatures_indices[t]) - 1]

                    if answers[i] == 0:
                        answers[i] = closest_index - i
                    else:
                        answers[i] = int(min(answers[i], closest_index - i))

            # otherwise, answers[i] will remain 0 which is the correct answer

        return answers


class Solution2:
    def dailyTemperatures(self, temperatures: [int]) -> [int]:
        if len(temperatures) <= 0:
            return []

        answers = [0] * len(temperatures)

        for i in range(len(temperatures) - 2, -1, -1):
            # at each step we check if the current_temp is < or > the one after it
            if temperatures[i] < temperatures[i + 1]:
                # then the answer is easy, we just put 1
                answers[i] = 1
            else:
                # the current temperature is higher than the one after it
                # we need to use the answers we've accumulated so far to solve the problem

                # since temp[i] > temp[i+1], then temp[i]'s answer lies after temp[i+1]'s answer
                if answers[i + 1] > 0:
                    # we do this check to make sure that there is an element greater in the future
                    # otherwise there's no reason to check
                    index_to_check = (i + 1) + answers[i + 1]

                    while index_to_check < len(temperatures) and answers[index_to_check] > 0 and temperatures[index_to_check] <= temperatures[i]:
                        # we need to keep jumping forward until we find a temperature
                        # greater than the current one
                        index_to_check = index_to_check + answers[index_to_check]

                    # we exited the loop so we either found our answer or we exceeded the array
                    if index_to_check < len(temperatures) and temperatures[index_to_check] > temperatures[i]:
                        # it means we broke the loop because we found our answer
                        # the biggest temp after the current one is at index_to_check
                        answers[i] = index_to_check - i

        return answers


# temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
# temperatures = [30,40,50,60]
# temperatures = [30,60,90]
# temperatures = [60, 50, 40, 30]
# temperatures = [55,38,53,81,61,93,97,32,43,78]
#              [0, 3, 2, 1, 1,  0, 1,  0, 3, 2, 1, 0, 0, 2, 1,  0]
temperatures = [77,55,48,30,77,100,31,100,69,60,47,95,68,47,33,64]
print(Solution2().dailyTemperatures(temperatures))


# Output
# [3,1,1,4,3,1,1,3,1,1,1,1,30,1,3,2,1,25,2,1,19,2,1,3,2,1,11,5,1,1,2,1,3,2,1,2,1,2,1,3,2,1,0,0,3,1,1,1,0,0,5,1,1,2,1,0,1,10,5,1,2,1,1,4,3,1,1,11,1,1,8,1,1,5,1,3,1,1,0,1,3,2,1,1,0,3,2,1,1,0,1,0,3,2,1,0,0,2,1,0]

# Expected
# [3,1,1,4,3,1,1,3,1,1,1,1,30,1,3,2,1,25,2,1,19,2,1,3,2,1,11,5,1,1,2,1,3,2,1,2,1,2,1,3,2,1,0,46,3,1,1,1,30,18,5,1,1,2,1,12,1,10,5,1,2,1,1,4,3,1,1,11,1,1,8,1,1,5,1,3,1,1,11,1,3,2,1,1,5,3,2,1,1,0,1,0,3,2,1,0,0,2,1,0]

# print(len(temperatures))
# expected = [0, 3, 2, 1, 1, 0, 1, 0, 3, 2, 1, 0, 0, 2, 1, 0]
# output = [5, 3, 2, 1, 1, 0, 1, 0, 3, 2, 1, 0, 0, 2, 1, 0]

# for i in range(len(expected) - 1, -1, -1):
#     if expected[i] != output[i]:
#         print(str(len(expected) - i))
#         break
