import heapq
from string import ascii_letters

mapping = dict(zip(ascii_letters, range(len(ascii_letters))))
mapping["S"] = mapping['a']
mapping["E"] = mapping['z']


def build_graph(input: str, reversed=False):
    grid = input.split('\n')
    graph = {}

    start, end = '', []
    m, n = len(grid), len(grid[0])
    for i in range(m):
        for j in range(n):
            node = grid[i][j]
            if reversed:
                if node == 'E':
                    start = (i, j)
                if node == 'a':
                    end.append((i, j))
            else:
                if node == 'S':
                    start = (i, j)
                if node == 'E':
                    end = (i, j)
            for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if (i + x >= 0) and (j + y >= 0):
                    try:
                        target = grid[i + x][j + y]
                        if reversed:
                            if mapping[node] - 1 <= mapping[target]:
                                graph.setdefault((i, j), []).append((i + x, j + y))
                            else:
                                graph.setdefault((i, j), [])
                        else:
                            if mapping[node] + 1 >= mapping[target]:
                                graph.setdefault((i, j), []).append((i + x, j + y))
                            else:
                                graph.setdefault((i, j), [])
                    except:
                        pass
    return graph, start, end


def dijkstra(graph, start):
    inf = float('inf')
    prev, dist = {}, {}
    dist[start] = 0
    q = []
    for v, edges in graph.items():
        if v != start:
            dist[v] = inf
            prev[v] = None
        heapq.heappush(q, (dist[v], v))

    while q:
        node = heapq.heappop(q)[1]
        for v in graph[node]:
            alt = dist[node] + 1
            if alt < dist[v]:
                heapq.heappush(q, (alt, v))
                dist[v] = alt
                prev[v] = node
    return dist, prev
