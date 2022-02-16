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

