# Implement Travelling Salesman Problem using the nearest-neighbor heuristic.
# Input: The input Graph is provided in the form of a 2-D matrix (adjacency matrix).
# Consider the first node as the starting point.
# Output: A list of indices indicating the path taken. You must return the sequence of
# nodes, the path taken starting from node 0. In this example, G is 5x5, indicating
# there are 5 nodes in this graph: 0-4. You will always begin with node 0, and your
# path should include every node exactly once, and only go between nodes with a
# nonzero edge between them. You path will end at the starting node.

def solve_tsp(G):
    """
    Solves the TSP problem above using nearest neighbor heuristic.
    :param G: A  connected graph, like:
    G = [
        [0, 2, 3, 20, 1],
        [2, 0, 15, 2, 20],
        [3, 15, 0, 20, 13],
        [20, 2, 20, 0, 9],
        [1, 20, 13, 9, 0],
        ]
    :return: A list of indices indicating the path taken, like:
    [0, 4, 3, 1, 2, 0]
    """
    # create false array for each node we need to visit
    nodes = len(G)
    visited = [False]*nodes
    # start at node 0
    visited[0] = True
    res = [0]
    # for the current node we find the nearest unvisited node and move there
    for i in range(nodes-1):
        current = res[-1]
        next_dist = float('inf')
        next_node = None

        for neighbor in range(nodes):
            if visited[neighbor]:
                continue
            if 0 < G[current][neighbor] < next_dist:
                next_dist = G[current][neighbor]
                next_node = neighbor

        res.append(next_node)
        visited[next_node] = True

    #return back to the start for cycle
    res.append(0)
    return res

if __name__ == '__main__':
    G1 = [
        [0, 2, 3, 20, 1],
        [2, 0, 15, 2, 20],
        [3, 15, 0, 20, 13],
        [20, 2, 20, 0, 9],
        [1, 20, 13, 9, 0]
    ]
    #passed
    p1 = solve_tsp(G1)
    print(p1)