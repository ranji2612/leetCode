# Clone Graph
# https://leetcode.com/problems/clone-graph/

# Definition for a undirected graph node
# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution(object):
    reached = {}
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if node==None:
            return None
        x = UndirectedGraphNode(node.label)
        self.reached[node] = x
        
        for i in node.neighbors:
            if not i in self.reached:
                y = self.cloneGraph(i)
                if y!=None:
                    x.neighbors.append(y)
            else:
                x.neighbors.append(self.reached[i])
        return x