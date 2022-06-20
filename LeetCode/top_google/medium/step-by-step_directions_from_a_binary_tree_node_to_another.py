'''
    https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

    2096. Step-By-Step Directions From a Binary Tree Node to Another

    You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n.
    You are also given an integer startValue representing the value of the start node s, and a different integer
    destValue representing the value of the destination node t.

    Find the shortest path starting from node s and ending at node t.
    Generate step-by-step directions of such path as a string consisting of only the uppercase letters 'L', 'R', and 'U'.
    Each letter indicates a specific direction:
        - 'L' means to go from a node to its left child node.
        - 'R' means to go from a node to its right child node.
        - 'U' means to go from a node to its parent node.

    Return the step-by-step directions of the shortest path from node s to node t.
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
    Accepted. But, I want to try to do it without the Graph class.
'''


class Solution:
    class Graph:
        V = None  # list of vertices in Graph
        E = None  # list of edges in Graph

        def __init__(self):
            self.V = set()
            self.E = {}  # maps vertices to the vertices related to them

        def add_vertex(self, u):
            self.V.add(u)

        # we don't define a weight now because we're working with unweighted graph
        def add_edge(self, u, v, type):
            if u not in self.V:
                self.V.add(u)

            if v not in self.V:
                self.V.add(v)

            if u not in self.E:
                self.E[u] = set()

            if v not in self.E:
                self.E[v] = set()

            # we add both edges because we are working now with an undirected graph
            # from u to v is a parent to child relationship and we add the type of the child to the edge
            # type == L or type == R
            self.E[u].add((v, type))
            # from v to u is a parent to child relationship and we add the type of relationship as up
            self.E[v].add((u, 'U'))

        # returns list of vertices adjacent to u in the graph
        def get_adjacent(self, u):
            # return the list of vertices adjacent to u
            if u in self.E:
                return list(self.E[u])

            return []

        # does BFS to get the shortest path between s and all other vertices
        def bfs(self, s):
            WHITE = 0
            GREY = 1
            BLACK = 2

            color = {}
            distance = {}
            parent = {}

            for u in self.V:
                # initialize every vertex except for the source vertex
                if u != s:
                    color[u] = WHITE
                    distance[u] = float("-inf")
                    parent[u] = (None, None)

            # initialize the source vertex
            color[s] = GREY
            distance[s] = 0
            parent[s] = (None, None)

            # initialize empty list
            Q = []

            # add the source vertex to the queue
            Q.append(s)

            # now we keep iterating over the vertices in the queue until the queue is empty
            while len(Q) != 0:
                # the vertex we need to now explore
                u = Q.pop(0)

                # before exploring the vertex, we first need to add its unvisited neighbors to the queue so they
                # can be explored next
                u_adjacency = self.get_adjacent(u)

                for v, type in u_adjacency:
                    # this guarantees that we don't re-explore discovered or explored vertices
                    if color[v] == WHITE:
                        color[v] = GREY
                        distance[v] = distance[u] + 1
                        parent[v] = (u, type)

                        Q.append(v)

                # now that we're not exploring u, we mark it as explored
                color[u] = BLACK

            return parent

    def getDirections(self, root: [TreeNode], startValue: int, destValue: int) -> str:
        if root is None:
            return ""

        # we need to build the graph out of the tree
        G = self.Graph()

        Q = []
        Q.append(root)

        while len(Q) != 0:
            node = Q.pop(0)

            # add the node as a vertex in the graph
            G.add_vertex(node.val)

            # add the children of this vertex as adjacent to its in the graph
            if node.left is not None:
                Q.append(node.left)
                G.add_edge(node.val, node.left.val, 'L')

            if node.right is not None:
                Q.append(node.right)
                G.add_edge(node.val, node.right.val, 'R')

        # now that we are done with setting up the graph, we need to run bfs with our given source node: startValue
        parent = G.bfs(startValue)

        # now we need to traverse the parent relations from destValue backwards until we reach the source node startValue
        path = ""

        node = destValue

        while node != startValue:
            if parent[node] != (None, None):
                path = parent[node][1] + path

                node = parent[node][0]
            else:
                # we can't reach s from the destination node, so we return empty string
                return ""

        return path


'''
    Accepted and with better performance because removed unnecessary data: distance, color turned to visited, graph.
'''


class Solution2:
    def bfs(self, adjacent, n, s):
        visited = set()
        parent = {}

        # the nodes we have go from 1 to n
        for u in range(1, n + 1):
            # initialize every vertex except for the source vertex
            if u != s:
                parent[u] = (None, None)

        # initialize the source vertex
        visited.add(s)
        parent[s] = (None, None)

        # initialize empty list
        Q = []

        # add the source vertex to the queue
        Q.append(s)

        # now we keep iterating over the vertices in the queue until the queue is empty
        while len(Q) != 0:
            # the vertex we need to now explore
            u = Q.pop(0)

            # before exploring the vertex, we first need to add its unvisited neighbors to the queue so they
            # can be explored next
            u_adjacency = adjacent[u]

            for v, type in u_adjacency:
                # this guarantees that we don't re-explore discovered or explored vertices
                if v not in visited:
                    visited.add(v)
                    parent[v] = (u, type)

                    Q.append(v)

        return parent

    def getDirections(self, root: [TreeNode], startValue: int, destValue: int) -> str:
        if root is None:
            return ""

        # maps every node to its adjacent nodes (children + parent => because undirectional graph)
        adjacent = {}
        n = 0

        Q = []
        Q.append(root)

        while len(Q) != 0:
            node = Q.pop(0)

            # to count the number of nodes we have
            n += 1

            if node.val not in adjacent:
                adjacent[node.val] = set()

            # add the children of this vertex as adjacent to its in the graph
            if node.left is not None:
                Q.append(node.left)

                if node.left.val not in adjacent:
                    adjacent[node.left.val] = set()

                # add the child relation
                adjacent[node.val].add((node.left.val, 'L'))
                # add the parent relation
                adjacent[node.left.val].add((node.val, 'U'))

            if node.right is not None:
                Q.append(node.right)

                if node.right.val not in adjacent:
                    adjacent[node.right.val] = set()

                # add the child relation
                adjacent[node.val].add((node.right.val, 'R'))
                # add the parent relation
                adjacent[node.right.val].add((node.val, 'U'))

        # now that we are done with creating our adjacency relations, we need to run bfs with our given source node: startValue
        parent = self.bfs(adjacent, n, startValue)

        # now we need to traverse the parent relations from destValue backwards until we reach the source node startValue
        path = ""

        node = destValue

        while node != startValue:
            if parent[node] != (None, None):
                path = parent[node][1] + path

                node = parent[node][0]
            else:
                # we can't reach s from the destination node, so we return empty string
                return ""

        return path


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)

node5.left = node1
node5.right = node2

node1.left = node3

node2.left = node6
node2.right = node4

print(Solution().getDirections(node5, 3, 6))
