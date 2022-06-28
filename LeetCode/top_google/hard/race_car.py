'''
    https://leetcode.com/problems/race-car/

    818. Race Car

    Your car starts at position 0 and speed +1 on an infinite number line. Your car can go into negative positions.
    Your car drives automatically according to a sequence of instructions 'A' (accelerate) and 'R' (reverse):

    When you get an instruction 'A', your car does the following:
        - position += speed
        - speed *= 2

    When you get an instruction 'R', your car does the following:
        - If your speed is positive then speed = -1
        - otherwise speed = 1

        Your position stays the same.

    For example, after commands "AAR", your car goes to positions 0 --> 1 --> 3 --> 3, and your speed goes to 1 --> 2 --> 4 --> -1.

    Given a target position target, return the length of the shortest sequence of instructions to get there.
'''

'''
    We need to explore all sequences of A and R to see which one is the minimum out of them in length.
    
    While we are building the sequences, we need to make sure that we're not going in directions that will only further distance
    us from our goal. In other words, if the target > current position then we need to A to move forward. If the target < current position
    then we need to R to go backwards. Otherwise, we might end up with infinite sequences or with sequences of more length than what we need.
'''


class Solution:
    def racecar(self, target: int) -> int:
        Q = []

        # we will append elements in the queue in the form of (position, speed, level)
        # the starting (position, speed, level) are (0, +1, 0')
        Q.append((0, 1, 0))

        # will go through the level of our tree and at each node, we have 2 branches coming out:
        # - the branch where our next instruction is A
        # - the branch where our next instruction is R

        # when we reach a level where our position == target, we return with the current depth of the node as solution
        while len(Q) != 0:
            currentPosition, currentSpeed, currentLevel = Q.pop(0)

            if currentPosition == target:
                return currentLevel
            else:
                # we need to continue by branching

                # taking A as the next branch
                # if not ((currentPosition > target and currentSpeed > 0) or (currentPosition < target and currentSpeed < 0)):
                Q.append((currentPosition + currentSpeed, currentSpeed * 2, currentLevel + 1))

                # taking R as the next branch ONLY IF
                # - the next position of A > target and speed > 0, then we can't A anymore because we'd be just exceeding the target
                # - the next position of A < target and speed < 0, then we can't A anymore because we'd be going further away from target

                # Otherwise, R is just a waste of time

                if (currentPosition + currentSpeed) > target and currentSpeed > 0:
                    # reverse
                    Q.append((currentPosition, -1, currentLevel + 1))

                if (currentPosition + currentSpeed) < target and currentSpeed < 0:
                    # reverse
                    Q.append((currentPosition, 1, currentLevel + 1))


print(Solution().racecar(330))
