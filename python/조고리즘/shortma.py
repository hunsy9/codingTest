import sys
import heapq

edge = int(sys.stdin.readline())
INF = 1e8
min_cycle_distance = 1e8
min_cycle = []
graph = {}
for i in range(97,123):
    graph[chr(i)] = {}
for i in range(edge):
    sp, ep, weight = sys.stdin.readline().split()
    graph[sp][ep] = int(weight)
    graph[ep][sp] = int(weight)
vertex_list = graph.keys()
vertex_num = len(vertex_list)
print(graph)
def find_cycle(start):
    distances = {node: float('inf') for node in graph}
    queue = []
    # heapq.heappush(queue, [distances[start], start])
    # while queue:
    #     node = queue.pop()
    #     for adj_node in graph_dict.get(node):



