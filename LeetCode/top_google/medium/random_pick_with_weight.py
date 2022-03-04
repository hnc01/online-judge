'''
    https://leetcode.com/problems/random-pick-with-weight/

    You are given a 0-indexed array of positive integers w where w[i] describes the weight of the ith index.

    You need to implement the function pickIndex(), which randomly picks an index in the range [0, w.length - 1] (inclusive)
    and returns it. The probability of picking an index i is w[i] / sum(w).

    For example, if w = [1, 3], the probability of picking index 0 is 1 / (1 + 3) = 0.25 (i.e., 25%), and the probability
    of picking index 1 is 3 / (1 + 3) = 0.75 (i.e., 75%).

'''

import random

'''
    Time limit exceeded
'''


class Solution:
    probabilities = []

    def __init__(self, w: [int]):
        self.probabilities = [0] * len(w)

        weights_sum = sum(w)

        for i in range(0, len(w)):
            self.probabilities[i] = w[i] / weights_sum

    def pickIndex(self) -> int:
        return random.choices(list(range(0, len(self.probabilities))), weights=self.probabilities, k=1)[0]


'''
    Target: Sampling data such that the value of the data point determines of the probability of it being picked.
    => In other words, the probability that a number got picked is proportional to the value of the number, with 
       regards to the total sum of all numbers.

    The task is to do sampling with weights.

    If one comes across this problem during an interview, one can consider the problem almost resolved, once one reduces the 
    original problem down to the problem of inserting an element into a sorted list.
    
    Explanation of why prefixSum works:

    Think that if we had an array [1,2,3,4,3]. Normal random pickIndex would pick any index from 0 to 4 with equal probability. 
    But we want that index=1 is picked by 2/13 probability, index=0 with 1/13 probability and so on. (13 is sum of weights). 
    To ensure that one way to think of it if we make a larger array (of size 13) where the values are the indices such that index i is 
    repeated w[i] times then if we do a normal rand on this array then index 0 to 12 will be picked randomly with equal probability. 
    13 index array -> [0, 1,1, 2,2,2, 3,3,3,3, 4,4,4]. So there is a 3/13 chance of picking 2 as 2 is repeated thrice in the new array.
    
    Now instead of actually constructing this 13 index array, we just know the range of the index of the 13 index array where value = i. Eg:
    
    for index=0, range is {0,0}
    index =1, range of indices of the new array is {1,2}
    index=2, range={3,5}
    index=3, range ={6,9}
    index = 4, range = {10,12}
    In other words,
    
    index=0, range is <1
    index=1, range is <3
    index=2, range is <6
    index = 3, range is < 10
    index = 4, range is < 13
    
    If you notice the above numbers 1,3,6,10,13 - they are cumulative sum.
    The reason this happens is because for every range: right = left + (w[i] - 1) and left is (prev right+1). 
    So if we substitute 2nd equation into 1st. right = (prev right)+w[i]; i.e. keep adding prev sum to current weight.
    
    Thus the prefixSum is able to implement this.
'''

'''
    Accepted
'''


class Solution2:
    prefix_sums = None
    total_sum = 0

    def __init__(self, w: [int]):
        self.prefix_sums = [0] * len(w)

        total_sum = 0

        for i in range(0, len(w)):
            self.prefix_sums[i] = total_sum + w[i]

            total_sum += w[i]

        # now we know the prefix's range is from 0 to all_sum since
        # the prefixes is just the sum of all the numbers incrementally
        self.total_sum = total_sum

    def pickIndex(self) -> int:
        # this will generate numbers from 0 to the max sum that we have but without actually giving us the last prefix_sum
        # if we use int, then we'd be losing the range between the last 2 prefix sums and if we include the last prefix_sum
        # then that won't be correct because then we'd risk never returning in the loop target < prefix_sum
        # TODO this is important to use otherwise WA
        target = self.total_sum * random.random()

        # TODO note that using enumerate here instead of for i in range(0, len(self.prefix_sums) got us ACCEPTED instead of time limit exceeded
        # now we go through the list of prefix sums and see the first one bigger than target
        # it means that `target` belongs in place of the prefix_sum we found
        for i, prefix_sum in enumerate(self.prefix_sums):
            if target < prefix_sum:
                # this is the right index to place target_offset in the list of prefix_sums
                return i


# Your Solution object will be instantiated and called as such:
w = [1, 3]
# w = [1]
# w = [5,1,9,4,1]
obj = Solution2(w)
print(obj.pickIndex())
