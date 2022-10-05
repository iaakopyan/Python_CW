import math
#Напишите функцию, которая ищет кратчайший путь из вершины А в вершину Б ориентированного графа, заданного матрицей смежности

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, s, d, w):
        self.graph.append([s, d, w])

    @staticmethod
    def print_solution(dist, fin):
        if math.isinf(dist[fin]):
            print(None)
        else:
            print(dist[fin])

    def bellman_ford(self, src, fin):

        dist = [float("Inf")] * self.V
        dist[src] = start

        for _ in range(self.V - 1):
            for s, d, w in self.graph:
                if dist[s] != float("Inf") and dist[d] > dist[s] + w:
                    dist[d] = dist[s] + w
        for s, d, w in self.graph:
            if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                return None

        self.print_solution(dist, fin)


N, start, finish = (int(i) for i in input().split())
start -= 1
finish -= 1
A = []
for i in range(N):
    a = map(int, input().split(maxsplit=N))
    a = list(a)
    A.append(a)

g = Graph(N)
for i in range(0, N):
    for j in range(0, N):
        if A[i][j] > 0:
            g.add_edge(i, j, A[i][j])

g.bellman_ford(start, finish)

