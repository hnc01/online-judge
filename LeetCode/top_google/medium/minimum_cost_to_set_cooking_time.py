'''
    https://leetcode.com/problems/minimum-cost-to-set-cooking-time/

    2162. Minimum Cost to Set Cooking Time

    A generic microwave supports cooking times for:
    - at least 1 second.
    - at most 99 minutes and 99 seconds.
    - To set the cooking time, you push at most four digits. The microwave normalizes what you push as four digits
      by prepending zeroes. It interprets the first two digits as the minutes and the last two digits as the seconds.
      It then adds them up as the cooking time. For example,

    - You push 9 5 4 (three digits). It is normalized as 0954 and interpreted as 9 minutes and 54 seconds.
    - You push 0 0 0 8 (four digits). It is interpreted as 0 minutes and 8 seconds.
    - You push 8 0 9 0. It is interpreted as 80 minutes and 90 seconds.
    - You push 8 1 3 0. It is interpreted as 81 minutes and 30 seconds.

    You are given integers startAt, moveCost, pushCost, and targetSeconds. Initially, your finger is on the digit startAt.
    Moving the finger above any specific digit costs moveCost units of fatigue. Pushing the digit below the finger once costs pushCost
    units of fatigue.

    There can be multiple ways to set the microwave to cook for targetSeconds seconds but you are interested in the way with the minimum cost.

    Return the minimum cost to set targetSeconds seconds of cooking time.

    Remember that one minute consists of 60 seconds.
'''

'''
    Accepted
'''


class Solution:
    def generateRepresentationsHelper(self, minutes, seconds):
        minutesOptions = []
        secondsOptions = []

        if minutes < 10:
            # we only have 1 digit in minutes
            minutesOptions.append([minutes])

            # since we have only 1 digit we have the option of prepending a 0
            minutesOptions.append([0, minutes])

            if minutes == 0:
                minutesOptions.append([])
        else:
            # we have 2 digits in minutes so we can't prepend 0s
            minutesOptions.append([minutes // 10, minutes % 10])

        if seconds < 10:
            # we must prepend a 0 to seconds otherwise the result is wrong
            secondsOptions.append([0, seconds])
        else:
            # seconds is 2 digits
            secondsOptions.append([seconds // 10, seconds % 10])

        representations = []

        # now we have to combine each minute option with every seconds option
        for minutesOption in minutesOptions:
            for secondsOption in secondsOptions:
                representations.append(minutesOption + secondsOption)

        return representations

    def generateRepresentations(self, targetSeconds: int):
        representations = []

        minutes = targetSeconds // 60
        seconds = targetSeconds % 60

        if minutes > 0:
            # we can make use of the minutes field
            # here we have 2 options: either use minutes with OPTIONAL seconds field OR use minutes with FORCED seconds field
            if minutes > 99:
                # use minutes with FORCED seconds field
                while minutes > 99 and seconds + 60 <= 99:
                    minutes -= 1
                    seconds += 60

                representations.extend(self.generateRepresentationsHelper(minutes, seconds))

                while True:
                    # we also need to consider the option of removing from the minutes field and adding to the seconds field 60 seconds
                    if minutes > 0 and seconds + 60 <= 99:
                        minutes -= 1
                        seconds += 60

                        representations.extend(self.generateRepresentationsHelper(minutes, seconds))
                    else:
                        break
            else:
                # either use minutes with OPTIONAL seconds
                representations.extend(self.generateRepresentationsHelper(minutes, seconds))

                while True:
                    # we also need to consider the option of removing from the minutes field and adding to the seconds field 60 seconds
                    if minutes > 0 and seconds + 60 <= 99:
                        minutes -= 1
                        seconds += 60

                        representations.extend(self.generateRepresentationsHelper(minutes, seconds))
                    else:
                        break
        else:
            # can only use the seconds field
            # since the target can fit all in just seconds, then this generates 3 options for us: seconds alone, 0 + seconds, 00 + seconds
            representations.append([targetSeconds // 10, targetSeconds % 10])
            representations.append([0, targetSeconds // 10, targetSeconds % 10])
            representations.append([0, 0, targetSeconds // 10, targetSeconds % 10])

            if targetSeconds < 10:
                # we have the option of having the seconds alone without any prepends
                representations.append([targetSeconds])
        # else:
        # target seconds < 60 and so it would have been caught by our targetSeconds < 99 code block

        return representations

    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        minCost = float('inf')

        representations = self.generateRepresentations(targetSeconds)

        # now is the time to generate for each representation, 2 representations: push and move
        for representation in representations:
            moveRepresentation = []

            # push representation are all the buttons we need to press to get our representation
            # it's always equal to the representation itself while ignoring the startAt button because
            # if it's part of the representation then we will push and if it's not then we won't

            # move representation are all the buttons we are moving towards
            # we always have at targetSeconds >= 1 so know we never have an empty representation
            if startAt != representation[0]:
                moveRepresentation.append(startAt)

            for digit in representation:
                # if we are pushing the same button multiple times in a row, then we don't need to move to it
                if (len(moveRepresentation) > 0 and digit != moveRepresentation[-1]) or (len(moveRepresentation) == 0):
                    moveRepresentation.append(digit)

            # finally the cost of this representation is = moveCost * len(moveRepresentation) + pushCost * len(representation = pushRepresentation)
            minCost = min(minCost, moveCost * (len(moveRepresentation) - 1) + pushCost * len(representation))

        return minCost


# print(Solution().minCostSetTime(startAt=1, moveCost=2, pushCost=1, targetSeconds=600))
# print(Solution().minCostSetTime(startAt=0, moveCost=1, pushCost=2, targetSeconds=76))
# print(Solution().minCostSetTime(startAt=0, moveCost=1, pushCost=2, targetSeconds=42))
# print(Solution().minCostSetTime(startAt=0, moveCost=1, pushCost=4, targetSeconds=9))
print(Solution().minCostSetTime(7, 220, 479, 6000))
