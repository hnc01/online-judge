'''
    https://leetcode.com/problems/odd-even-jump/

    975. Odd Even Jump

    You are given an integer array arr. From some starting index, you can make a series of jumps. The (1st, 3rd, 5th, ...)
    jumps in the series are called odd-numbered jumps, and the (2nd, 4th, 6th, ...) jumps in the series are called even-numbered jumps.
    Note that the jumps are numbered, not the indices.

    You may jump forward from index i to index j (with i < j) in the following way:
        - During odd-numbered jumps (i.e., jumps 1, 3, 5, ...), you jump to the index j such that arr[i] <= arr[j] and arr[j] is the smallest possible value. If there are multiple such indices j, you can only jump to the smallest such index j.
        - During even-numbered jumps (i.e., jumps 2, 4, 6, ...), you jump to the index j such that arr[i] >= arr[j] and arr[j] is the largest possible value. If there are multiple such indices j, you can only jump to the smallest such index j.
        - It may be the case that for some index i, there are no legal jumps.

    A starting index is good if, starting from that index, you can reach the end of the array (index arr.length - 1) by jumping some number
    of times (possibly 0 or more than once).

    Return the number of good starting indices.
'''

'''
    First, we'll do a brute force solution without any optimizations.
    
    Correct answers but TLE as expected.
'''


class Solution:
    def oddEvenJumps(self, arr: [int]) -> int:
        n = len(arr) - 1

        goodJumpsCount = 0

        for i in range(0, len(arr)):
            currentNumber = arr[i]

            jumpCount = 1
            currentPosition = i

            while True:
                if currentPosition == n:
                    goodJumpsCount += 1
                    break
                else:
                    if jumpCount % 2 == 0:
                        # even jump
                        # from i+1 to n, search for largest number smaller than currentNumber.
                        # in case of duplicates, keep only the smallest j.
                        jumpToValue = float('-inf')
                        jumpToIndex = -1

                        for j in range(currentPosition + 1, len(arr)):
                            if arr[j] <= currentNumber and arr[j] > jumpToValue:
                                jumpToValue = arr[j]
                                jumpToIndex = j
                    else:
                        # odd jump
                        # from i+1 to n, search for smallest number larger than currentNumber.
                        # in case of duplicates, keep only the smallest j.
                        jumpToValue = float('inf')
                        jumpToIndex = -1

                        for j in range(currentPosition + 1, len(arr)):
                            if arr[j] >= currentNumber and arr[j] < jumpToValue:
                                jumpToValue = arr[j]
                                jumpToIndex = j

                    if jumpToIndex != -1:
                        # we have a valid jump so we can take it
                        currentPosition = jumpToIndex
                        currentNumber = arr[currentPosition]
                        jumpCount += 1
                    else:
                        # we can't make any further jumps from this position
                        break

        return goodJumpsCount


'''
    Keep track of 2 structures: 
    - isGoodEvenJump[i] = True if we can reach the end of the array by starting with even jump at index i. False otherwise.
    - isGoodOddJump[i] = True if we can reach the end of the array by starting with odd jump at index i. False otherwise.
    
    Maybe start by filling these arrays from the end to the start.
    isGoodEvenJump[n] = True => we can for sure reach the end of the array if we start from end of array.
    isGoodOddJump[n] = True => we can for sure reach the end of the array if we start from end of array.
    
    then for i from n-1 to 0, we check where we land if we do an odd jump from arr[i] or even jump from arr[i].
    - We will land on arr[n] => in which case the jump is good => True
    - We will land on some arr[j] that is precomputed => jump of i is same result as jump of j.
'''

'''
    Still TLE because we take too long to find our next jump => O(n2)
'''


class Solution2:
    def doJumps(self, arr, i, n, isEvenJump, isGoodEvenJump, isGoodOddJump):
        currentNumber = arr[i]

        currentPosition = i

        if isEvenJump:
            # even jump
            # from i+1 to n, search for largest number smaller than currentNumber.
            # in case of duplicates, keep only the smallest j.
            jumpToValue = float('-inf')
            jumpToIndex = -1

            for j in range(currentPosition + 1, len(arr)):
                if arr[j] <= currentNumber and arr[j] > jumpToValue:
                    jumpToValue = arr[j]
                    jumpToIndex = j
        else:
            # odd jump
            # from i+1 to n, search for smallest number larger than currentNumber.
            # in case of duplicates, keep only the smallest j.
            jumpToValue = float('inf')
            jumpToIndex = -1

            for j in range(currentPosition + 1, len(arr)):
                if arr[j] >= currentNumber and arr[j] < jumpToValue:
                    jumpToValue = arr[j]
                    jumpToIndex = j

        if jumpToIndex != -1:
            # first flip the jump type because we already did one jump
            isEvenJump = not isEvenJump

            # we have a valid jump, check if we can reach the end from
            # the new position by checking our memo structures
            if isEvenJump:
                # check the even jumps structure
                return isGoodEvenJump[jumpToIndex]
            else:
                # check the odd jumps structure
                return isGoodOddJump[jumpToIndex]
        else:
            # we can't make any further jumps from this position
            return False

    def oddEvenJumps(self, arr: [int]) -> int:
        n = len(arr) - 1

        isGoodEvenJump = [False] * len(arr)
        isGoodOddJump = [False] * len(arr)

        # we know that we can reach the end by start at the end
        isGoodOddJump[n] = True
        isGoodEvenJump[n] = True

        # to count already for the jump from n to n
        goodJumpsCount = 1

        for i in range(n - 1, -1, -1):
            # from this number try to start with even jump and see if we land at the end
            isGoodEvenJump[i] = self.doJumps(arr, i, n, True, isGoodEvenJump, isGoodOddJump)

            # from this number try to start with odd jump and see if we land at the end
            isGoodOddJump[i] = self.doJumps(arr, i, n, False, isGoodEvenJump, isGoodOddJump)

            # total number of good jumps only depends on the isGoodOddJump True values because
            # the 1st jump is always odd
            if isGoodOddJump[i]:
                goodJumpsCount += 1

        return goodJumpsCount


'''
    Accepted.
    
    Used sorting (O(nlog)) to substitute the O(n^2) we were spending to find the element to jump to.
    Used isGoodEvenJump and isGoodOddJump to memorize previously computed jumps.
'''


class Solution3:
    def doJump(self, sortedArray, i, isGoodEvenJump, isGoodOddJump):
        currentNumber, currentNumberIndex = sortedArray[i]

        jumpSequence = []

        # our first jump is always odd
        isEvenJump = False

        while True:
            # while looping, if we encounter the last element in the array, it means we reached the end so true
            if currentNumberIndex == (len(sortedArray) - 1):
                # success we reached the end, mark everything as true and return
                for elementIndex, elementIsEvenJump in jumpSequence:
                    if elementIsEvenJump:
                        isGoodEvenJump[elementIndex] = True
                    else:
                        isGoodOddJump[elementIndex] = True

                # finally we set our own jump value
                # this was an even jump so we set the right memo
                if isEvenJump:
                    isGoodEvenJump[currentNumberIndex] = True
                else:
                    isGoodOddJump[currentNumberIndex] = True

                return

            # we find the nextElement we're going to jump to
            if isEvenJump:
                # even jump
                # from i+1 to n, search for largest number smaller than currentNumber.
                # in case of duplicates, keep only the smallest j.

                # find the first element smaller than or equal to current element but has bigger index (i.e. comes after it)
                # to cover the equal case, in order for a number to be equal with bigger index than current element,
                # it has to be right after it in sortedArray

                # first we cover our equal case
                equalElementIndex = -1

                if (i + 1) < len(sortedArray) and sortedArray[i + 1][0] == currentNumber:
                    equalElementIndex = i + 1

                if equalElementIndex != -1 and equalElementIndex < len(sortedArray):
                    # this will be the largest element <= to our element so no need to look further
                    nextElementIndex = equalElementIndex
                else:
                    # since there's nothing equal to our element that has index bigger, we need to find something smaller
                    # largest number smaller than current number is at i - 1
                    nextElementIndex = i - 1

                    while nextElementIndex >= 0 and sortedArray[nextElementIndex][1] < currentNumberIndex:
                        nextElementIndex -= 1

                    if nextElementIndex >= 0:
                        # we found our next element => smaller than our current element but index is larger
                        nextElement = sortedArray[nextElementIndex]

                        # after we find the element, we need to keep going backwards as long as we have duplicate values of this element
                        while nextElementIndex >= 0 and sortedArray[nextElementIndex][0] == nextElement[0] and sortedArray[nextElementIndex][1] > currentNumberIndex:
                            nextElementIndex -= 1

                        # when we hit the end => we either exceeded the array limits or found an element not equal
                        # we do backIndex + 1 to go back to our element
                        nextElementIndex += 1
                    else:
                        # could not find a next element to jump to so entire sequence is False
                        for elementIndex, elementIsEvenJump in jumpSequence:
                            if elementIsEvenJump:
                                isGoodEvenJump[elementIndex] = False
                            else:
                                isGoodOddJump[elementIndex] = False

                        # finally we set our own jump value
                        # this was an even jump so we set the right memo
                        isGoodEvenJump[currentNumberIndex] = False

                        return
            else:
                # odd jump
                # from i+1 to n, search for smallest number larger than currentNumber.
                # in case of duplicates, keep only the smallest j.
                # the smallest number larger than or equal to current number is at i + 1 onwards
                nextElementIndex = i + 1

                while nextElementIndex < len(sortedArray) and sortedArray[nextElementIndex][1] < currentNumberIndex:
                    nextElementIndex += 1

                if nextElementIndex >= len(sortedArray):
                    # could not find a next element to jump to so entire sequence is False
                    for elementIndex, elementIsEvenJump in jumpSequence:
                        if elementIsEvenJump:
                            isGoodEvenJump[elementIndex] = False
                        else:
                            isGoodOddJump[elementIndex] = False

                    # finally we set our own jump value
                    # this was an odd jump so we set the right memo
                    isGoodOddJump[currentNumberIndex] = False

                    return

            # since we didn't return after finding the next element, it means we have a valid index
            nextElement = sortedArray[nextElementIndex]

            # depending on our jump type, we check the right structure to see if we solved nextElement or not yet
            if isEvenJump:
                # we check the odd jumps for next element
                isValidNextElementJump = isGoodOddJump[nextElement[1]]
            else:
                # we check the even jumps for next element
                isValidNextElementJump = isGoodEvenJump[nextElement[1]]

            if isValidNextElementJump is not None:
                # we already solved this problem for the next element so we take its value it and set the same for the sequence
                for elementIndex, elementIsEvenJump in jumpSequence:
                    if elementIsEvenJump:
                        isGoodEvenJump[elementIndex] = isValidNextElementJump
                    else:
                        isGoodOddJump[elementIndex] = isValidNextElementJump

                # finally we set our own jump value
                # this was an even jump so we set the right memo
                if isEvenJump:
                    isGoodEvenJump[currentNumberIndex] = isValidNextElementJump
                else:
                    isGoodOddJump[currentNumberIndex] = isValidNextElementJump

                # we are done with computing for this jump so we return
                return
            else:
                # we haven't solved for this element so we need to keep solving
                # we need to compute the value so we have to make the jump and see what happens
                # our next jump is even so we do an even jump
                # we add to sequence that we did an odd jump from i
                jumpSequence.append((currentNumberIndex, isEvenJump))

                # flip the jump type for next iteration
                isEvenJump = not isEvenJump

                # we have a valid jump so we can take it
                currentNumber, currentNumberIndex = sortedArray[nextElementIndex]

                # update i to be the position in sortedArray of next element
                i = nextElementIndex

    def oddEvenJumps(self, arr: [int]) -> int:
        # first we will sort the elements in arr by value in asc and then by index in asc
        sortedArray = []

        for i in range(0, len(arr)):
            sortedArray.append((arr[i], i))

        sortedArray.sort()

        # index of last element in array
        n = len(arr) - 1

        # now that we have our sorted array, it will be easy for us to find the next jump location
        isGoodEvenJump = [None] * len(arr)
        isGoodOddJump = [None] * len(arr)

        # we know that we can reach the end by start at the end
        isGoodOddJump[n] = True
        isGoodEvenJump[n] = True

        goodJumpsCount = 0

        # we will use this loop to go through the elements in sortedArray
        for i in range(0, len(sortedArray)):
            if isGoodOddJump[sortedArray[i][1]] is None:
                # from this number we start with odd jump and see if we end up at the end of array
                self.doJump(sortedArray, i, isGoodEvenJump, isGoodOddJump)

            # total number of good jumps only depends on the isGoodOddJump True values because
            # the 1st jump is always odd
            if isGoodOddJump[sortedArray[i][1]]:
                goodJumpsCount += 1

        return goodJumpsCount


# print(Solution3().oddEvenJumps(arr=[10, 13, 12, 14, 15]))
# print(Solution3().oddEvenJumps(arr=[2, 3, 1, 1, 4]))
# print(Solution3().oddEvenJumps(arr=[5, 1, 3, 4, 2]))
# print(Solution3().oddEvenJumps(arr=[9, 10, 13, 12, 14, 15, 14]))
# print(Solution3().oddEvenJumps(arr=[5,6,1,2,56,32,23,40,34]))
print(Solution3().oddEvenJumps(arr=[5, 6, 1, 2, 56, 32, 23, 40, 34, 28972, 52180, 97908, 16647, 92940, 41477, 88034, 37389, 91815, 88125, 83067, 32933]))
# for long submission, the expected is: 16023
