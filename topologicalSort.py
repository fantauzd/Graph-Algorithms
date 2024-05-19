# Dominic Fantauzzo

from collections import defaultdict

class Graph:
    # Constructor
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.vertices = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)


def topoSort(G):
    """
    Perform a topographical sort on a directed acyclic graph
    :param G: Graph
    :return:
    """
    # Mark all the vertices as not visited
    visited = [False] * G.vertices
    # Our stack to store the result/output
    result = []

    for currentNode in range(G.vertices):
        if visited[currentNode] == False:
            topoHelper(G, currentNode, visited, result)

    return (result)

def topoHelper(G, currentNode, visited, result):
    visited[currentNode] = True
    # Recur for all the adjacent vertices of currentNode
    for i in G.graph[currentNode]:
        if visited[i] == False:
            topoHelper(G, i, visited, result)
    # Push current vertex to result
    result.insert(0, currentNode)






if __name__ == '__main__':
    # create a graph
    myGraph = Graph(5)
    myGraph.addEdge(0, 1)
    myGraph.addEdge(0, 3)
    myGraph.addEdge(1, 2)
    myGraph.addEdge(2, 3)
    myGraph.addEdge(2, 4)
    myGraph.addEdge(3, 4)
    print(topoSort(myGraph))