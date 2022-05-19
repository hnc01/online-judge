'''
    https://leetcode.com/problems/battleships-in-a-board/

    419. Battleships in a Board

    Given an m x n matrix board where each cell is a battleship 'X' or empty '.', return the number of the battleships on board.

    Battleships can only be placed horizontally or vertically on board. In other words, they can only be made of the shape 1 x k
    (1 row, k columns) or k x 1 (k rows, 1 column), where k can be of any size. At least one horizontal or vertical cell separates
    between two battleships (i.e., there are no adjacent battleships).
'''

'''
    Accepted
'''


class Solution:
    class Graph:
        adjacency = None
        vertices = None

        def __init__(self):
            self.adjacency = {}  # mapping each vertex to its adjacent vertices
            self.vertices = set()

        def add_vertex(self, i, j):
            self.vertices.add((i, j))

        def add_edge(self, source, destination):
            if source in self.adjacency:
                self.adjacency[source].add(destination)
            else:
                temp = set()
                temp.add(destination)
                self.adjacency[source] = temp

            if destination in self.adjacency:
                self.adjacency[destination].add(source)
            else:
                temp = set()
                temp.add(source)
                self.adjacency[destination] = temp

        def dfs_visit(self, vertex, visited):
            visited.add(vertex)

            adjacent_vertices = []

            if vertex in self.adjacency:
                adjacent_vertices = self.adjacency[vertex]

            for adjacent_vertex in adjacent_vertices:
                if adjacent_vertex not in visited:
                    self.dfs_visit(adjacent_vertex, visited)

        def connected_components(self):
            visited = set()

            component_roots_count = 0

            for (i, j) in self.vertices:
                if (i, j) not in visited:
                    component_roots_count += 1

                    self.dfs_visit((i, j), visited)

            return component_roots_count

    def countBattleships(self, board: [[str]]) -> int:
        g = self.Graph()

        # length of grid is at least one cell so we're sure this will never fail
        m = len(board)  # rows
        n = len(board[0])  # cols

        for i in range(0, m):
            for j in range(0, n):
                if board[i][j] == 'X':
                    # always add the current node
                    g.add_vertex(i, j)

                    # check if there are any vertices up, down, left or right
                    # above = (i - 1, j) # already passed through it so has a node + the edge
                    # left = (i, j - 1) # already passed through it so has a node + the edge

                    if i + 1 < m:
                        # under = (i + 1, j)
                        # the cell exists
                        if board[i + 1][j] == 'X':
                            # we need to add it to graph
                            g.add_vertex(i + 1, j)
                            # we need to add an edge between current node and under
                            g.add_edge((i, j), (i + 1, j))

                    if j + 1 < n:
                        # right = (i, j + 1)
                        # the cell exists
                        if board[i][j + 1] == 'X':
                            # we need to add it to graph
                            g.add_vertex(i, j + 1)
                            # we need to add an edge between current node and under
                            g.add_edge((i, j), (i, j + 1))

        # we are done with constructing the graph, now we need to call `connected components algorithm`
        return g.connected_components()


print(Solution().countBattleships([["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]]))
print(Solution().countBattleships([["X", "X", ".", "X"], [".", ".", ".", "X"], ["X", ".", ".", "X"]]))
print(Solution().countBattleships([["."]]))
