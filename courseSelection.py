class Solution(object):
    time=0
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        taken = {}
        courses = []
        adjList = []
        #Initializing
        for i in range(numCourses):
            courses.append(i)
            taken[i] = 'WHITE'
            adjList.append([])
        #Bulding the adj List
        for i in prerequisites:
            adjList[i[0]].append(i[1])
        
        #Topology Sort
        def dfsVisit(n):
            taken[n] = 'GREY'
            status = True
            for node in adjList[n]:
                if taken[node]=='GREY':
                    #cycle existis
                    return False
                status = status and dfsVisit(node)
            taken[n] = 'BLACK'
            return status
        #Calling Topo Sort
        for course in courses:
            if taken[course]=='WHITE':
                status = dfsVisit(course)
                if not status:
                    return False
        return True
            