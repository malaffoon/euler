"""Problem 107 - Project Euler

Minimal network

The following undirected network consists of seven vertices and twelve edges with a total weight of 243.
The same network can be represented by the matrix below.
   	A	B	C	D	E	F	G
A	-	16	12	21	-	-	-
B	16	-	-	17	20	-	-
C	12	-	-	28	-	31	-
D	21	17	28	-	18	19	23
E	-	20	-	18	-	-	11
F	-	-	31	19	-	-	27
G	-	-	-	23	11	27	-
However, it is possible to optimise the network by removing some edges and still ensure that all
points on the network remain connected. The network which achieves the maximum saving is shown
below. It has a weight of 93, representing a saving of 243 − 93 = 150 from the original network.

Using network.txt (right click and 'Save Link/Target As...'), a 6K text file containing a network
with forty vertices, and given in matrix form, find the maximum saving which can be achieved by
removing redundant edges whilst ensuring that the network remains connected.

--------------------------------------------------------------------------------------------------

Appears to be a straightforward MST problem. Use Prim's or Kruskal's to find the answer.
Could use scipy package. Or i could code it myself. Prim's, at least, is easy enough if we aren't
worried too much about performance. I wish i had my SRI graph library, dang it!
"""

PROBLEM107_EXAMPLE = [
    [None, 16, 12, 21, None, None, None],
    [16, None, None, 17, 20, None, None],
    [12, None, None, 28, None, 31, None],
    [21, 17, 28, None, 18, 19, 23],
    [None, 20, None, 18, None, None, 11],
    [None, None, 31, 19, None, None, 27],
    [None, None, None, 23, 11, 27, None],
]


class Problem107(object):
    @staticmethod
    def solve(graph=None):
        # read graph as an adjacency matrix of edge weights
        if graph is None:
            with open('../../resources/p107_network.txt') as file:
                graph = [[None if w == '-' else int(w) for w in line.strip().split(',')] for line in file.readlines()]
        # assert that it is a square matrix
        if len(graph[0]) != len(graph) or any(len(row) != len(graph[0]) for row in graph):
            raise ValueError("bad network data")

        n = len(graph)

        # calculate the original total weight (upper diagonal)
        original_sum = sum(graph[i][j] for i in range(0, n) for j in range(0, n) if graph[i][j]) // 2

        # use Prim's to build up the MST edges, accumulating the sum of those edge weights
        min_sum = 0
        nodes = [0]
        while len(nodes) < n:
            min_node, min_weight = None, 1000
            for node in nodes:
                for idx, weight in enumerate(graph[node]):
                    if weight is None or idx in nodes:
                        continue
                    if weight < min_weight:
                        min_node, min_weight = idx, weight
            nodes.append(min_node)
            min_sum += min_weight
        return original_sum - min_sum

    @staticmethod
    def get_tests():
        return [(PROBLEM107_EXAMPLE, 150), (None, 259679)]


if __name__ == '__main__':
    print("The answer is", Problem107.solve())
    # hmmm, example works fine but real graph gives me 261832 - 7714
    # oh, nodes 1 and 2 don't seem to be pulled into the graph?
