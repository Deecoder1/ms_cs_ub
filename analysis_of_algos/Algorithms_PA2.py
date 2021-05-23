class Graph:
# We use this calss to represent the graph and hold all the attributes.
    def __init__(self, vertices):
        try:
            # We store the number of vertices and the list to store the graph details.
            self.V, self.graph = vertices, []
        except Exception as e:
            return e
    def add_an_edge(self, src, dest, weight):
        # This function is used to add an edge to the graph.
        try:
            self.graph.append([src, dest, weight])
        except Exception as e:
            return e
    def find(self, parent, i):
        # We use this function to find the set of an element i.
        try:
            return i if parent[i] == i else self.find(parent, parent[i])
        except Exception as e:
            return e
    def union(self, parent, rank, x, y):
        # This function unions the two sets x and y.
        try:
            x_root, y_root = self.find(parent, x), self.find(parent, y)
            if rank[x_root] > rank[y_root]:
                parent[y_root] = x_root
            elif rank[x_root] < rank[y_root]:
                parent[x_root] = y_root
            else:
                parent[y_root] = x_root
                rank[x_root] += 1
        except Exception as e:
            return e
    def Kruskal_MST(self):
        # We initialize the variables that hold the MST, an indexing variable, edge iterator.
        result, i, ed, n  = [], 0, 0, 0
        parent,rank = [], []
        self.graph = sorted(self.graph, key=lambda item: item[2])
        while n < self.V:
            parent.append(n)
            rank.append(0)
            n+=1
        while ed < self.V -1:
            src, dest, weight = self.graph[i]
            i += 1
            parent_src, parent_dest = self.find(parent, src), self.find(parent, dest)
            if parent_src != parent_dest:
                result.append([src, dest, weight])
                self.union(parent, rank, parent_src, parent_dest)
                ed += 1
        minCost = 0
        for weight in result:
            minCost += weight[2]
        print(minCost)
        for src, dest, weight in result:
            print(src+1, dest+1)
 
# Taking Input from STDIN
nodes, edges = map(int, input().split())
g = Graph(nodes)
for i in range(edges):
    src, dest, weight = map(int, input().split())
    g.add_an_edge(src-1,dest-1,weight)

g.Kruskal_MST()

# References:
# [1] https://en.wikipedia.org/wiki/Kruskal%27s_algorithm
# [2] https://www.tutorialspoint.com/data_structures_algorithms/kruskals_spanning_tree_algorithm.htm
# [3] https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/
# [4] https://www.baeldung.com/cs/kruskals-vs-prims-algorithm