'''
    https://leetcode.com/problems/number-of-islands/

    200. Number of Islands

    Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

    An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.

    You may assume all four edges of the grid are all surrounded by water.
'''

'''
    time limit exceeded no matter how much we reduce so this is not the right answer
'''

'''
    TODO Try turning the grid into a graph where connected nodes are adjacent 1s and then run a `connected components`
    algorithm on the graph to get the nb of islands
'''


class Solution:
    def get_islands(self, islands, i, j):
        # this function checks if (i,j) belongs to an existing island

        # (i,j) belongs to island if island contains any of the following coordinates: (i-1,j) (i,j+1) (i+1,j) (i,j-1)
        # i.e. any of the points above, under, left or right of (i,j) => vertical + horizontal
        above = (i - 1, j)
        # under = (i + 1, j) => no need to check under because we go through the grid from top to bottom
        # right = (i, j + 1) => no need to check right because we go through the grid from left to right
        left = (i, j - 1)

        islands_indices = []
        merged_islands = set()

        for k in range(0, len(islands)):
            island = islands[k]

            if above in island or left in island:
                islands_indices.append(k)
                merged_islands.update(island)

        # island indices always in sorted order
        return (islands_indices, merged_islands)

    def numIslands(self, grid: [[str]]) -> int:
        islands = []  # this will be a list of sets and each set is comprised of coordinates of the points that makeup an island

        # we know that we always have at least one cell in the grid based on the given of the problem
        m = len(grid)  # number of rows
        n = len(grid[0])  # number of columns

        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == '1':
                    island_indices, merged_islands = self.get_islands(islands, i, j)

                    if len(island_indices) > 0:
                        merged_islands.add((i, j))
                        islands.append(merged_islands)

                        deleted_count = 0

                        # take them in ascending order
                        for index in island_indices:
                            # every time we remove an element we need to decrease the other indices
                            new_index = index - deleted_count
                            del islands[new_index]
                            deleted_count += 1
                    else:
                        # we create a new island for this point
                        temp = set()
                        temp.add((i, j))

                        islands.append(temp)

        return len(islands)


class Solution2:
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

    def numIslands(self, grid: [[str]]) -> int:
        g = self.Graph()

        # length of grid is at least one cell so we're sure this will never fail
        m = len(grid)  # rows
        n = len(grid[0])  # cols

        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == '1':
                    # always add the current node
                    g.add_vertex(i, j)

                    # check if there are any vertices up, down, left or right
                    # above = (i - 1, j) # already passed through it so has a node + the edge
                    # left = (i, j - 1) # already passed through it so has a node + the edge

                    if i + 1 < m:
                        # under = (i + 1, j)
                        # the cell exists
                        if grid[i + 1][j] == '1':
                            # we need to add it to graph
                            g.add_vertex(i + 1, j)
                            # we need to add an edge between current node and under
                            g.add_edge((i, j), (i + 1, j))

                    if j + 1 < n:
                        # right = (i, j + 1)
                        # the cell exists
                        if grid[i][j + 1] == '1':
                            # we need to add it to graph
                            g.add_vertex(i, j + 1)
                            # we need to add an edge between current node and under
                            g.add_edge((i, j), (i, j + 1))

        # we are done with constructing the graph, now we need to call `connected components algorithm`
        return g.connected_components()


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]

# grid = [
#     ["1", "1", "0", "0", "0"],
#     ["1", "1", "0", "0", "0"],
#     ["0", "0", "1", "0", "0"],
#     ["0", "0", "0", "1", "1"]
# ]

# grid = [
#     ["1", "1", "1", "1", "1"],
#     ["1", "1", "1", "1", "1"],
#     ["1", "1", "1", "1", "1"],
#     ["1", "1", "1", "1", "1"]
# ]

# grid = [
#     ["0", "0", "0", "0", "0"],
#     ["0", "0", "0", "0", "0"],
#     ["0", "0", "0", "0", "0"],
#     ["0", "0", "0", "0", "0"]
# ]

# grid = [
#     ["0", "1", "1", "1"],
#     ["1", "0", "1", "0"],
#     ["0", "1", "1", "1"]
# ]

# grid = [
#     ["1", "0", "1", "1", "1"],
#     ["1", "0", "1", "0", "1"],
#     ["1", "1", "1", "0", "1"]
# ]

# grid = [
#     ["1", "1", "1"],
#     ["0", "1", "0"],
#     ["1", "1", "1"]
# ]

# TODO add diagonal check and if diagonal is in the island and the element under the diagonal is a 1 then they are part of the same island

print(Solution2().numIslands(grid))
