'''
    https://leetcode.com/problems/maximum-split-of-positive-even-integers/

    2178. Maximum Split of Positive Even Integers

    You are given an integer finalSum. Split it into a sum of a maximum number of unique positive even integers.

    For example, given finalSum = 12, the following splits are valid (unique positive even integers summing up to finalSum):
    (12), (2 + 10), (2 + 4 + 6), and (4 + 8). Among them, (2 + 4 + 6) contains the maximum number of integers.
    Note that finalSum cannot be split into (2 + 2 + 4 + 4) as all the numbers should be unique.

    Return a list of integers that represent a valid split containing a maximum number of integers.
    If no valid split exists for finalSum, return an empty list. You may return the integers in any order.
'''

'''
    The below solution is correct but for sure TLE.
'''


class Solution:
    def maximumEvenSplitHelper(self, finalSum, evenNumber, currentSplit, splits):
        if finalSum == 0:
            # we are done and have found a valid split
            splits.append(currentSplit)
        elif finalSum >= evenNumber:
            # it means that we can still a possible solution by moving forward
            # however, if we reach a point where evenNumber > finalSum then we can't reach a solution
            # because evenNumber will only increase with every recursive call

            # at this stage, we need to consider 2 options:
            # we either consider evenNumber as part of our split and see if we get a solution
            newCurrentSplit = currentSplit.copy()
            newCurrentSplit.append(evenNumber)

            self.maximumEvenSplitHelper(finalSum - evenNumber, evenNumber + 2, newCurrentSplit, splits)

            # or we ignore evenNumber and consider the next number instead
            self.maximumEvenSplitHelper(finalSum, evenNumber + 2, currentSplit, splits)
        # else: finalSum < evenNumber => no possible valid splits so abandon path

    def maximumEvenSplit(self, finalSum: int) -> [int]:
        # from the start, we know that every odd number can't be split into a sum of even numbers
        if finalSum % 2 == 1:
            return []

        # now that we're sure that finalSum is even, we can proceed
        allSplits = []
        self.maximumEvenSplitHelper(finalSum, 2, [], allSplits)

        maxSplit = []
        maxSplitLength = 0

        for split in allSplits:
            if len(split) > maxSplitLength:
                maxSplit = split
                maxSplitLength = len(split)

        return maxSplit


'''
    Observations:
    - Since we are looking for maximum length split, then it makes more sense that it would be made up of the smallest even numbers.
    - All we need to do is find the smallest even number that can generate valid splits and then take the longest split.
    - When we are generating the possible splits starting at a number, we need to stop if we found a valid sequence using the smallest integers.
    
    The below is correct but it needs too much recursion depth. Can we do it sequentially? or can we memorize some branches?
'''


class Solution2:
    def maximumEvenSplitHelper(self, finalSum, evenNumber, currentSplit):
        if finalSum == 0:
            # we are done and have found a valid split
            return currentSplit
        elif finalSum >= evenNumber:
            # it means that we can still a possible solution by moving forward
            # however, if we reach a point where evenNumber > finalSum then we can't reach a solution
            # because evenNumber will only increase with every recursive call

            # at this stage, we need to consider 2 options:
            # we either consider evenNumber as part of our split and see if we get a solution
            newCurrentSplit = currentSplit.copy()
            newCurrentSplit.append(evenNumber)

            includeCurrentNumberSolution = self.maximumEvenSplitHelper(finalSum - evenNumber, evenNumber + 2, newCurrentSplit)

            if len(includeCurrentNumberSolution) > 0:
                # in our first go through (which always picks smallest even numbers), we found a solution => it's the maximum
                return includeCurrentNumberSolution
            else:
                # try to ignore the evenNumber and consider the next number instead
                ignoreCurrentNumberSolution = self.maximumEvenSplitHelper(finalSum, evenNumber + 2, currentSplit)

                if len(ignoreCurrentNumberSolution):
                    return ignoreCurrentNumberSolution
                else:
                    return []
        else:
            # else: finalSum < evenNumber => no possible valid splits so abandon path
            return []

    def maximumEvenSplit(self, finalSum: int) -> [int]:
        # from the start, we know that every odd number can't be split into a sum of even numbers
        if finalSum % 2 == 1:
            return []

        # now that we're sure that finalSum is even, we can proceed
        evenNumber = 2

        while True:
            # we need the split to contain evenNumber so we force it from the start
            currentNumberMaxSplit = self.maximumEvenSplitHelper(finalSum - evenNumber, evenNumber + 2, [evenNumber])

            # if we have len(allSplits) > 0 then we found valid sequences for smallest even number, get the longest one and return
            if len(currentNumberMaxSplit) > 0:
                return currentNumberMaxSplit
            else:
                # move on to the second even number
                evenNumber += 2


'''
    From all the above observations, I reached the below solution.
    
    The idea is that to find the maximum length split, it makes more sense that it would be made up of the smallest even numbers. 
    So, we start with the smallest integer and go up 2 at a time until we either reach finalSum or we exceed it. If we reach it then 
    the split we generated is the longest solution. If we exceed it, then we just remove from our split the integer equal to splitSum - finalSum.
'''


class Solution3:
    def maximumEvenSplit(self, finalSum: int) -> [int]:
        if finalSum % 2 == 1:
            return []

        split = []

        currentSum = 0
        evenNumber = 2

        while currentSum < finalSum:
            split.append(evenNumber)

            currentSum += evenNumber

            evenNumber += 2

        if currentSum == finalSum:
            return split
        else:
            # else finalSum < currentSum
            # remove the remainder from the split and return
            remainder = currentSum - finalSum

            # remove remainder from split
            split.pop((remainder // 2) - 1)

            return split


# print(Solution().maximumEvenSplit(28))
# print(Solution().maximumEvenSplit(12))
# print(Solution().maximumEvenSplit(7))
# print(Solution2().maximumEvenSplit(2000))
print(Solution3().maximumEvenSplit(6914017674))
