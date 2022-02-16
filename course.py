import collections

class Course:

    def findCourseOrderBFS(self, numCourses: int, prereqs: list[list[int]]) -> list[int]:
        graph, res, inDegree, queue = collections.defaultdict(list), [], [0] * numCourses, collections.deque()

        for pair in prereqs:
            graph[pair[1]].append(pair[0])
            inDegree[pair[0]] += 1

        for i in range(numCourses):
            if inDegree[i] == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()
            res.append(node)
            inDegree[node] -= 1

            for neigh in graph[node]:
                inDegree[neigh] -= 1
                if inDegree[neigh] == 0:
                    queue.append(neigh)


        return res if len(res) == numCourses else []



"""

example : numCourses = 4, prereqs = [[1,0], [2,0], [3,1], [3,2]]
output : [0,2,1,3]

logic below:
    
    graph = {}
    queue = []
    res = []
    inDegree = [0,0,0,0]

    for pair in prereqs:            pair: [1,0], [2,0], [3,1], [3,2]
      1st iteration:  
        pair[0], pair[1] = 1, 0
        graph[pair[1]].append(pair[0])
        graph[0] = [1]
        inDegree[pair[0]] += 1
        inDegree[0,1,0,0]
      
      2nd iteration:
        pair[0], pair[1] = 2, 0
        graph[pair[1]].append(pair[0])
        graph[0] = [1,2]
        inDegree[pair[0]] += 1
        inDegree[0, 1, 1, 0]

      3rd iteration:
        pair[0], pair[1] = 3, 1
        graph[pair[1]].append(pair[0])
        graph[1] = [3]
        inDegree[pair[0]] += 1
        inDegree[0, 1, 1, 1]

      4th iteration:
        pair[0], pair[1] = 3, 2
        graph[pair[1]].append(pair[0])
        graph[2] = [3]
        inDegree[pair[0]] += 1
        inDegree[0, 1, 1, 2]

    after iterations we have:

        graph = {0:[1,2] , 1: [3] , 2: [3] , 3: []}
        inDegree = [0, 1, 1, 2]


    Next we iterate through the indegree to check if we have a course with zero in degree which means that there is no prereqs for that class:
                                                IDX:   0, 1, 2, 3
        for i in range(numCourses):         inDegree: [0, 1, 1, 2]
            1st iteration:
                i = 0
                inDegree[0] == 0
                queue.append(i)
                queue = [0]
                we append i since the inDegree at i is zero

            2nd iteration:
                i = 1
                inDegree[1] == 1
                we dont append since there is a prereq
                queue = [0]

            3rd iteration:
                i = 2
                inDegree[2] == 1
                we dont append since there is a prereq
                queue = [0]

            4th iteration:
                i = 3
                inDegree[3] == 2
                we dont append since there is a prereq
                queue = [0]

        queue = [0]


        Next we go through the queue to append to our result array in the order in which you must take the classes we will know if the class can be taken if its indegree is zero


              graph = {0:[1,2] , 1: [3] , 2: [3] , 3: []}
              inDegree = [0, 1, 1, 2]

                
            while queue:
            
                1st iteration:
                    queue = [0]
                    res = []
                    inDegree = [0, 1, 1, 2]

                    node = queue.popleft()          result after: queue = []
                    res.append(node)                result after: res = [0]        
                    inDegree[node] -= 1             result after: [-1, 1, 1, 2]

                    for neigh in graph[node]:       graph[0] = [1,2]
                        inDegree[neigh] -= 1        result after: [-1, 0, 0, 2]
                        if inDegree[neigh] == 0:
                            queue.append(neigh)     result after: queue = [1, 2]

                2nd iteration:
                    queue = [1,2]
                    res = [0]
                    inDegree = [-1, 0, 0, 2]
                    
                    node = queue.popleft()          result after: queue = []
                    res.append(node)                result after: res = [0, 1]
                    inDegree[node] -= 1             result after: [-1, -1, 1, 2]

                    for neigh in graph[node]:       graph[1] = [3]
                        inDegree[neigh] -= 1        result after = [-1, -1, 0, 1]
                        if inDegree[neigh] == 0:    False
                            queue.append(neigh)


                3rd iteration:
                    
                    queue = [2]
                    res = [0,1]
                    inDegree = [-1, -1, 0, 2]

                    node = queue.popleft()          result after: queue = []
                    res.append(node)                result after: res = [0, 1, 2]
                    inDegree[node] -= 1             result after: inDegree[-1, -1, -1, 1]

                    for neigh in graph[neigh]:       graph[2] = [3]
                        inDegree[neigh] -= 1        inDegree [-1, -1, -1, 0]
                        if inDegree[neigh] == 0:
                            queue.append(neigh)

                4th iteration:
                    queue = [3]
                    res = [0, 1, 2]
                    inDegree = [-1, -1, -1, 0]

                    node = queue.popleft()          result after: queue = []
                    res.append(node)                result after: res = [0, 1, 2, 3]
                    inDegree[node] -= 1             result after: [-1, -1, -1, -1]

                    for neigh in graph[node]:       graph[3] = []
                        does not run no neighbors


                breaks out of loop

            res = [0, 1, 2, 3]

            we return res if it is the same length of the number of courses, becuase if its smaller then we were not able to take all courses
                        








        


"""

