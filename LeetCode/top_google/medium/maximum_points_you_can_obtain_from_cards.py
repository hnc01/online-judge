'''
    https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

    1423. Maximum Points You Can Obtain from Cards

    There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.

    In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

    Your score is the sum of the points of the cards you have taken.

    Given the integer array cardPoints and the integer k, return the maximum score you can obtain.
'''

'''
    Correct but time limit exceeded. We need to memorize some of the computations.
'''


class Solution:
    def maxScoreHelper(self, cardPoints, k, l, r):
        print(str(l) + "," + str(r))
        # l is the index we're on from the left
        # r is the index we're on from the right

        # we keep looking for solution until we've drawn k cards
        if l + r < k:
            leftMaxScore = rightMaxScore = float('-inf')

            # trying the path of taking a card from the left
            if l < len(cardPoints):
                leftMaxScore = cardPoints[l] + self.maxScoreHelper(cardPoints, k, l + 1, r)

            # trying the path of taking a card from the right
            if r < len(cardPoints):
                rightMaxScore = cardPoints[(r + 1) * -1] + self.maxScoreHelper(cardPoints, k, l, r + 1)

            # returning the max out of both paths
            return max(leftMaxScore, rightMaxScore)
        else:
            return 0

    def maxScore(self, cardPoints: [int], k: int) -> int:
        # quick case to handle
        if k == len(cardPoints):
            return sum(cardPoints)

        # we need to try all possible combinations of:
        # taking k cards from the left
        # taking k cards from the right
        # taking n cards from the left and m cards from the right such that n + m = k
        return self.maxScoreHelper(cardPoints, k, 0, 0)


'''
    Accepted.
    
    I tried using a matrix to compute all the cases of taking n from the front and m from the back such that n + m = k. This meant that the
    matrix was k x k matrix and I was computing all possible max scores that in the area above the right diagonal of the matrix. The first issue
    was that we didn't actually need to memorize all the solutions in the matrix because all we kept referring to were the values along row 0
    and the values along col 0. This meant that we don't need to matrix we just need to memorize col 0 (front prefix sum) and row 0 (back prefix sum).
    This helped me get rid of the memory limit exceeded. After figuring out that I don't need to memorize all results, I remembered that not all combinations
    from [0 .. n] and [0 .. m] are valid because anything n + m < k is not a valid solution. Knowing that the only time we have n + m = k is on the
    right diagonal of the matrix solution, meant that the only scores we need to keep track of are the scores on this diagonal and none other. This
    helped reduce the computation time and lead to an accepted solution. 
'''


class Solution2:
    def maxScore(self, cardPoints: [int], k: int) -> int:
        # quick case to handle
        if k == len(cardPoints):
            return sum(cardPoints)

        # we create the prefix sum of pulling cards from the front and pulling cards from the back
        # front_prefix_sum[i] is the score of taking i cards from the front
        front_prefix_sum = [0] * (k + 1)  # we need k to be an index
        # back_prefix_sum[i] is the score of taking i cards from the back
        back_prefix_sum = [0] * (k + 1)  # we need k to be an index

        # this variable will keep track of the max score we've seen so far
        max_score = 0

        # we can prefill the front_prefix_sum[i] by taking all cards from the front
        # we can prefill the back_prefix_sum[i] by taking all cards from the back
        # front_prefix_sum[i] and back_prefix_sum[i] by default should remain 0 because it means taking 0 cards
        for i in range(1, k + 1):
            # taking one card from the back
            back_prefix_sum[i] = back_prefix_sum[i - 1] + cardPoints[-i]
            # taking one card from the front
            front_prefix_sum[i] = front_prefix_sum[i - 1] + cardPoints[i - 1]

            max_score = max(max_score, max(back_prefix_sum[i], front_prefix_sum[i]))

        # after checking the cases of taking all from back or all from front, we need to consider
        # the cases of pulling n from back and m from front st m + n = k => diagonal of matrix
        for i in range(1, k):
            max_score = max(max_score, back_prefix_sum[i] + front_prefix_sum[k - i])

        return max_score


print(Solution2().maxScore(cardPoints=[1, 2, 3, 4, 5, 6, 1], k=3))
print(Solution2().maxScore(cardPoints=[2, 2, 2], k=2))
print(Solution2().maxScore(cardPoints=[9, 7, 7, 9, 7, 7, 9], k=7))
print(Solution2().maxScore([30, 88, 33, 37, 18, 77, 54, 73, 31, 88, 93, 25, 18, 31, 71, 8, 97, 20, 98, 16, 65, 40, 18, 25, 13, 51, 59], 26))
