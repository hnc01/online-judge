'''
    https://leetcode.com/problems/rle-iterator/

    900. RLE Iterator

    We can use run-length encoding (i.e., RLE) to encode a sequence of integers. In a run-length encoded array of even length
    encoding (0-indexed), for all even i, encoding[i] tells us the number of times that the non-negative integer value encoding[i + 1]
    is repeated in the sequence.

    For example, the sequence arr = [8,8,8,5,5] can be encoded to be encoding = [3,8,2,5]. encoding = [3,8,0,9,2,5]
    and encoding = [2,8,1,8,2,5] are also valid RLE of arr.
    Given a run-length encoded array, design an iterator that iterates through it.

    Implement the RLEIterator class:

    - RLEIterator(int[] encoded) Initializes the object with the encoded array encoded.
    - int next(int n) Exhausts the next n elements and returns the last element exhausted in this way. If there is no element left
      to exhaust, return -1 instead.
'''

'''
    Accepted
'''


class RLEIterator:
    def __init__(self, encoding: [int]):
        # cleanup the encoding to remove all 0s at even locations and the element right after them
        self.encoding = []

        for i in range(0, len(encoding), 2):
            if encoding[i] > 0:
                self.encoding.append(encoding[i])
                self.encoding.append(encoding[i + 1])

        # the exhaust pointer is at the first the entry
        self.index = 0

    def next(self, n: int) -> int:
        if self.index >= len(self.encoding):
            return -1

        last_exhausted_element = -1

        # we still have elements to exhaust
        if self.encoding[self.index] > n:
            # we will remain in same position after exhausting current element
            self.encoding[self.index] -= n

            # self.index remains the same

            # return the current element because it's last one exhausted
            last_exhausted_element = self.encoding[self.index + 1]
        elif self.encoding[self.index] == n:
            self.encoding[self.index] -= n

            last_exhausted_element = self.encoding[self.index + 1]

            self.index += 2
        else:
            # self.encoding[self.index] < n
            # we might need to exhaust one or more characters
            while n > 0 and self.index < len(self.encoding):
                # know that current element is not 0

                if self.encoding[self.index] > n:
                    # we reached an element that's repeated more times than n
                    # we're done with our exhaustion
                    self.encoding[self.index] -= n
                    last_exhausted_element = self.encoding[self.index + 1]

                    # we're done with exhaustion
                    break
                elif self.encoding[self.index] == n:
                    # we reached an element that's repeated same amount as n
                    # we're done with our exhaustion
                    self.encoding[self.index] -= n

                    last_exhausted_element = self.encoding[self.index + 1]

                    self.index += 2

                    # we're done with exhaustion
                    break
                else:
                    # self.encoding[self.index] < n
                    # we're not done with our exhaustion

                    # exhaust the current element
                    n -= self.encoding[self.index]

                    # mark the current element as completely exhausted
                    self.encoding[self.index] = 0

                    # don't update the last exhausted element because we didn't reach it yet

                    # move on to the second element
                    self.index += 2

        return last_exhausted_element


# Your RLEIterator object will be instantiated and called as such:
encoding = [3, 8, 0, 9, 2, 5]

obj = RLEIterator(encoding)

# operations = ["next", "next", "next", "next"]
parameters = [[4], [1], [1], [2]]

for i in range(0, len(parameters)):
    print(obj.next(parameters[i][0]))
