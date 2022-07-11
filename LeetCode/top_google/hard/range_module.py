'''
    https://leetcode.com/problems/range-module/

    715. Range Module

    A Range Module is a module that tracks ranges of numbers. Design a data structure to track the ranges represented
    as half-open intervals and query about them.

    A half-open interval [left, right) denotes all the real numbers x where left <= x < right.

    Implement the RangeModule class:
    - RangeModule() Initializes the object of the data structure.
    - void addRange(int left, int right) Adds the half-open interval [left, right), tracking every real number in
    that interval. Adding an interval that partially overlaps with currently tracked numbers should add any numbers in
    the interval [left, right) that are not already tracked.
    - boolean queryRange(int left, int right) Returns true if every real number in the interval [left, right) is currently
    being tracked, and false otherwise.
    - void removeRange(int left, int right) Stops tracking every real number currently being tracked in the half-open
    interval [left, right).
'''

'''
    Accepted
'''


class RangeModule:
    ranges = None

    def __init__(self):
        self.ranges = []

    def addRange(self, left: int, right: int) -> None:
        # check if this new range can merge with any existing ranges
        newRanges = []

        newRange = (left, right)

        for range in self.ranges:
            isIntersection, mergedRange = self.getMergedRange(range, newRange)

            if isIntersection:
                newRange = mergedRange
            else:
                newRanges.append(range)

        newRanges.append(newRange)

        newRanges.sort()

        self.ranges = newRanges

    def queryRange(self, left: int, right: int) -> bool:
        # check if we have a range such that range[0] <= left and range[1] >= right
        for range in self.ranges:
            if range[0] <= left and range[1] >= right:
                return True

        return False

    def removeRange(self, left: int, right: int) -> None:
        newRanges = []

        # we have four cases:
        # case 1: |______xx|
        #               |xx_____|

        # case 2:       |xx_____|
        #         |______xx|

        # case 3: |____|xxx|____|
        # case 4: |xxxx|xxx|xxxx|
        toRemove = (left, right)

        for range in self.ranges:
            if toRemove is not None:
                if toRemove[0] <= range[0] and toRemove[1] >= range[0]:
                    # we are in cases 1 and 4
                    if toRemove[1] <= range[1]:
                        # we are in case 1
                        # what we will be left of our range is [toRemove[1] + 1, range[1])
                        if toRemove[1] != range[1]:
                            newRanges.append((toRemove[1], range[1]))

                        # there's nothing left from toRemove because everything from its left is explored
                        toRemove = None
                    else:
                        # we are in case 4
                        # the entire range is removed and we have possibly something left of toRemove
                        if range[1] != toRemove[1]:
                            # we don't append anything of the current range to newRanges
                            toRemove = (range[1], toRemove[1])
                        else:
                            toRemove = None
                elif toRemove[0] >= range[0] and toRemove[0] <= range[1]:
                    # we are in cases 2 and 3
                    if toRemove[1] >= range[1]:
                        # we are in case 2
                        # we have a new range to add to newRanges => what's left of our range
                        if range[0] != toRemove[0]:
                            newRanges.append((range[0], toRemove[0]))

                        # we need to keep intersecting whatever is left of toRemove
                        if range[1] != toRemove[1]:
                            toRemove = (range[1], toRemove[1])
                        else:
                            toRemove = None
                    else:
                        # we are in case 3
                        # we don't have anything left of toRemove but we end up with 2 new ranges (possibly)
                        if range[0] < toRemove[0]:
                            newRanges.append((range[0], toRemove[0]))

                        if toRemove[1] < range[1]:
                            newRanges.append((toRemove[1], range[1]))

                        toRemove = None
                else:
                    # we don't have any intersection with toRemove and the range so we keep the range as is
                    newRanges.append(range)
            else:
                # we already exhausted the toRemove range so we just add all the remaining ranges back
                newRanges.append(range)

        newRanges.sort()

        self.ranges = newRanges

    def getMergedRange(self, firstRange, secondRange):
        # first we need to make sure that firstRange < secondRange
        if firstRange[0] > secondRange[0]:
            firstRange, secondRange = secondRange, firstRange

        if secondRange[0] <= firstRange[1]:
            # we have an intersection
            return (True, (min(firstRange[0], secondRange[0]), max(firstRange[1], secondRange[1])))
        else:
            return (False, (None, None))


# Your RangeModule object will be instantiated and called as such:
obj = RangeModule()

instructions = ["addRange", "removeRange", "queryRange", "queryRange",
                "queryRange"]  # ,"removeRange","removeRange","removeRange","addRange","addRange","addRange","removeRange","addRange","queryRange","addRange","addRange","queryRange","queryRange","addRange","removeRange","removeRange","removeRange","queryRange","queryRange","addRange","addRange","queryRange","addRange","addRange","removeRange","addRange","addRange","queryRange","removeRange","queryRange","removeRange","addRange","addRange","queryRange","removeRange","removeRange","addRange","queryRange","queryRange","removeRange","removeRange","removeRange","queryRange","addRange","removeRange","removeRange","queryRange","removeRange","removeRange","queryRange","addRange","addRange","removeRange","queryRange","queryRange","addRange","removeRange","removeRange","addRange","addRange","addRange","addRange","queryRange","removeRange","addRange","addRange","addRange","queryRange","addRange","removeRange","queryRange","removeRange","removeRange","removeRange","queryRange","queryRange","queryRange","queryRange","queryRange","removeRange","queryRange","removeRange","queryRange","addRange","queryRange"]
params = [[14, 100], [1, 8], [77, 80], [8, 43], [4,
                                                 13]]  # ,[3,9],[45,49],[41,90],[58,79],[4,83],[34,39],[84,100],[8,9],[32,56],[35,46],[9,100],[85,99],[23,33],[10,31],[15,45],[52,70],[26,42],[30,70],[60,69],[10,94],[2,89],[26,39],[46,93],[30,83],[42,48],[47,74],[39,45],[14,64],[3,97],[16,34],[28,100],[19,37],[27,91],[55,62],[64,65],[2,48],[55,78],[21,89],[31,76],[13,32],[2,84],[21,88],[12,31],[89,97],[56,72],[16,75],[18,90],[46,60],[20,62],[28,77],[5,78],[58,61],[38,70],[24,73],[72,96],[5,24],[43,49],[2,20],[4,69],[18,98],[26,42],[14,18],[46,58],[16,90],[32,47],[19,36],[26,78],[7,58],[42,54],[42,83],[3,83],[54,82],[71,91],[22,37],[38,94],[20,44],[37,89],[15,54],[1,64],[63,65],[55,58],[23,44],[25,87],[38,85],[27,71]]

for i in range(0, len(instructions)):
    if instructions[i] == "addRange":
        obj.addRange(params[i][0], params[i][1])
    elif instructions[i] == "queryRange":
        print(obj.queryRange(params[i][0], params[i][1]))
    elif instructions[i] == "removeRange":
        obj.removeRange(params[i][0], params[i][1])
