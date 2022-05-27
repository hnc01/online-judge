'''
    https://leetcode.com/problems/time-needed-to-inform-all-employees/

    1376. Time Needed to Inform All Employees

        A company has n employees with a unique ID for each employee from 0 to n - 1. The head of the company is the one with headID.

    Each employee has one direct manager given in the manager array where manager[i] is the direct manager of the i-th employee,
    manager[headID] = -1. Also, it is guaranteed that the subordination relationships have a tree structure.

    The head of the company wants to inform all the company employees of an urgent piece of news. He will inform his direct subordinates,
    and they will inform their subordinates, and so on until all employees know about the urgent news.

    The i-th employee needs informTime[i] minutes to inform all of his direct subordinates (i.e., After informTime[i] minutes,
    all his direct subordinates can start spreading the news).

    Return the number of minutes needed to inform all the employees about the urgent news.
'''

'''
    Incorrect approach.
'''


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: [int], informTime: [int]) -> int:
        # we will traverse the tree in BFS style and at each level add the manager's total time

        # first we need to map each manager to his employees
        # the map will first map each employee to an empty list of subordinates
        managerToEmployee = {}

        for i in range(0, n):
            managerToEmployee[i] = []

        # then we go through the manager array and we fill the map
        for i in range(0, len(manager)):
            if manager[i] != -1:
                # we are not in the case of manager of company
                managerToEmployee[manager[i]].append(i)

        # now we can quickly access the subordinates of a manager by using the map

        # we will accumulate the total time using this variable
        totalTime = 0

        # the queue we will use to perform the BFS algorithm
        currentLevel = []

        # the BFS search starts with the manager of the entire company
        currentLevel.append(headID)
        currentLevelTotalTime = 0

        nextLevel = []

        while len(currentLevel) != 0:
            employee = currentLevel.pop(0)

            # get all the employee's subordinates
            subordinates = managerToEmployee[employee]

            if len(subordinates) > 0:
                # since this employee is a manager, we need to factor in his inform time
                # the level's total time is always the max among all the manager at this level
                currentLevelTotalTime = max(currentLevelTotalTime, informTime[employee])

                # then we add all his subordinates to the queue to be processed later
                for subordinate in subordinates:
                    nextLevel.append(subordinate)

            if len(currentLevel) == 0:
                # we are done with current level and we need to move on to the next level
                currentLevel = nextLevel.copy()
                # now we add up the level's total time to our overall total time
                totalTime += currentLevelTotalTime
                # reset next level
                nextLevel = []
                # reset the level's total time
                currentLevelTotalTime = 0

        return totalTime


'''
    BFS approach is not correct because the branches work in parallel. So, it's best to do DFS and see which branch needs the most time.
    
    Accepted.
'''


class Solution2:
    def traverseDFS(self, source, managerToEmployee, informTime):
        # first check if the current source has employees
        subordinates = managerToEmployee[source]

        if len(subordinates) > 0:
            # if we have subordinates then the total time of the branch is max of all outgoing branches
            branchTotalTime = 0

            for subordinate in subordinates:
                branchTotalTime = max(branchTotalTime, informTime[source] + self.traverseDFS(subordinate, managerToEmployee, informTime))

            return branchTotalTime
        else:
            # there no time needed to inform subordinates because they don't exist
            return 0

    def numOfMinutes(self, n: int, headID: int, manager: [int], informTime: [int]) -> int:
        # we will traverse the tree in DFS style and then check which branch needs the most time => that would be our result

        # first we need to map each manager to his employees
        # the map will first map each employee to an empty list of subordinates
        managerToEmployee = {}

        for i in range(0, n):
            managerToEmployee[i] = []

        # then we go through the manager array and we fill the map
        for i in range(0, len(manager)):
            if manager[i] != -1:
                # we are not in the case of manager of company
                managerToEmployee[manager[i]].append(i)

        return self.traverseDFS(headID, managerToEmployee, informTime)


print(Solution2().numOfMinutes(n=1, headID=0, manager=[-1], informTime=[0]))
print(Solution2().numOfMinutes(n=6, headID=2, manager=[2, 2, -1, 2, 2, 2], informTime=[0, 0, 1, 0, 0, 0]))
print(Solution2().numOfMinutes(15, 0, [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6], [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]))
print(Solution2().numOfMinutes(11, 4, [5, 9, 6, 10, -1, 8, 9, 1, 9, 3, 4], [0, 213, 0, 253, 686, 170, 975, 0, 261, 309, 337]))
