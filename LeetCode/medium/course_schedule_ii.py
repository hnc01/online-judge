'''
    https://leetcode.com/problems/course-schedule-ii/

    210. Course Schedule II

    There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
    You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
    Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.
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

        def dfs_visit_for_topological(self, u, topological_sort_order, visited, ancestry):
            # we are exploring u now so we need to mark it as grey
            visited.add(u)
            ancestry.add(u)

            adjacent_vertices = []

            if u in self.adjacency:
                adjacent_vertices = self.adjacency[u]

            # now discover every edge reachable from u
            for v in adjacent_vertices:
                if v not in visited:
                    if self.dfs_visit_for_topological(v, topological_sort_order, visited, ancestry) == True:
                        return True
                elif v in ancestry:
                    # we've seen this vertex AND its an ancestor
                    # if the edge is a backedge then we have a cycle
                    # i.e. the current node is linked back to an ancestor
                    return True

            # we're done exploring u
            ancestry.remove(u)

            topological_sort_order.insert(0, u)

            return False

        def dfs_for_topological(self):
            # set the is_topological to true so the function can insert the vertices
            # into the linked list topological_sort_order

            topological_sort_order = []
            visited = set()
            ancestry = set()

            # we dfs visit every undiscovered vertex in G
            for u in self.vertices:
                if u not in visited:
                    # dfs_visit_for_topological returns true if there are cycles
                    contains_cycles = self.dfs_visit_for_topological(u, topological_sort_order, visited, ancestry)

                    if contains_cycles:
                        return []

                    # else continue

            return topological_sort_order

    def findOrder(self, numCourses: int, prerequisites: [[int]]) -> [int]:
        g = self.Graph()

        for i in range(0, numCourses):
            g.add_vertex(i)

        for prerequisite in prerequisites:
            # we create an edge from prerequisite[1] to prerequisite[0]
            source = prerequisite[1]
            destination = prerequisite[0]

            # we need to take source course before we take destination course
            g.add_edge(source, destination)

        return g.dfs_for_topological()


numCourses = 2
prerequisites = [[1,0]]

numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]

numCourses = 1
prerequisites = []

numCourses = 2
prerequisites = [[1,0], [0,1]]

print(Solution().findOrder(numCourses, prerequisites))