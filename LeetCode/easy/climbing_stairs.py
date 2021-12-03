'''
    Start: Brute Force Approach
'''
'''
def climbStairsHelper(i, n):
    # n is the total goal to reach
    # i is the number of steps we've taken so far
    if i == n:
        return 1
    elif i > n:
        # if we take a step that exceeds n then we can't make that step => can't count path
        return 0
    else:
        return climbStairsHelper(i + 1, n) + climbStairsHelper(i + 2, n)


def climbStairs(n: int) -> int:
    return climbStairsHelper(0, n)
'''
'''
    End: Brute Force Approach
'''

'''
    Start: Brute Force + Memoization Approach [Accepted]
'''

def climbStairsHelper(i, n, memory):
    # n is the total goal to reach
    # i is the number of steps we've taken so far
    if i == n:
        return 1
    elif i > n:
        # if we take a step that exceeds n then we can't make that step => can't count path
        return 0
    elif memory[i] > 0:
        # we already counted the number of ways we can go from here
        return memory[i]
    else:
        memory[i] = climbStairsHelper(i + 1, n, memory) + climbStairsHelper(i + 2, n, memory)

        return memory[i]


def climbStairs(n: int) -> int:
    # the steps start from 1 and go all the way up to n so we need to be able to index n from the list
    memory = [0] * (n+1)

    return climbStairsHelper(0, n, memory)


'''
    End: Brute Force + Memoization Approach [Accepted]
    
    Analysis:
        In this way we are pruning recursion tree with the help of memo array and reducing the size of recursion tree up to n.
        
        Time-complexity: O(n)
        Space Compexity: O(n) [size of memory is O(n) + size of tree which is O(n) = 2O(n) = O(n)
'''
