'''
    https://leetcode.com/problems/course-schedule/

    207. Course Schedule

    There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
    Return true if you can finish all courses. Otherwise, return false.
'''


class Solution:
    class Graph:
        adjacency = None
        vertices = None

        def __init__(self):
            self.adjacency = {}  # mapping each vertex to its adjacent vertices
            self.vertices = set()

        def add_vertex(self, val):
            self.vertices.add(val)

        def add_edge(self, source, destination):
            if source in self.adjacency:
                self.adjacency[source].add(destination)
            else:
                temp = set()
                temp.add(destination)
                self.adjacency[source] = temp

        def dfs_visit(self, vertex, visited, ancestry):
            ancestry.add(vertex)
            visited.add(vertex)

            adjacent_vertices = []

            if vertex in self.adjacency:
                adjacent_vertices = self.adjacency[vertex]

            for adjacent_vertex in adjacent_vertices:
                if adjacent_vertex not in visited:
                    if self.dfs_visit(adjacent_vertex, visited, ancestry) == True:
                        return True
                elif adjacent_vertex in ancestry:
                    # we've seen this vertex AND its an ancestor
                    # if the edge is a backedge then we have a cycle
                    # i.e. the current node is linked back to an ancestor
                    return True

            # we are done with exploring branch that is root at this node so we no longer
            # need it in ancestry
            ancestry.remove(vertex)

            return False

        def detect_cycle(self):
            visited = set()

            for vertex in self.vertices:
                ancestry = set()  # reset ancestry with every new root of a DSF tree

                if vertex not in visited:
                    # if we detect a cycle in one of the DFS trees then we return True (there is a cycle)
                    if self.dfs_visit(vertex, visited, ancestry) == True:
                        return True

            # none of the DFS trees contained a cycle for False
            return False

    def canFinish(self, numCourses: int, prerequisites: [[int]]) -> bool:
        g = self.Graph()

        for i in range(0, numCourses):
            g.add_vertex(i)

        for prerequisite in prerequisites:
            # we create an edge from prerequisite[1] to prerequisite[0]
            source = prerequisite[1]
            destination = prerequisite[0]

            # we need to take source course before we take destination course
            g.add_edge(source, destination)

        if g.detect_cycle():
            # we can't take all courses if we have a cycle
            return False
        else:
            return True


numCourses = 2
prerequisites = [[1,0]]

# numCourses = 2
# prerequisites = [[1,0],[0,1]]

print(Solution().canFinish(numCourses, prerequisites))