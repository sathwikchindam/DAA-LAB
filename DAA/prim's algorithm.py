# Prim's Algorithm

def prim(graph):
    n = len(graph)
    selected = [False] * n
    selected[0] = True

    total_cost = 0

    print("Edges in Minimum Spanning Tree:")

    for _ in range(n - 1):
        minimum = float('inf')
        x = 0
        y = 0

        for i in range(n):
            if selected[i]:
                for j in range(n):
                    if not selected[j] and graph[i][j] != 0:
                        if graph[i][j] < minimum:
                            minimum = graph[i][j]
                            x = i
                            y = j

        print(x, "--", y, "=", minimum)

        total_cost += minimum
        selected[y] = True

    print("Total Cost of MST:", total_cost)


# Weighted adjacency matrix
graph = [
    [0, 2, 3, 0, 0],
    [2, 0, 1, 4, 0],
    [3, 1, 0, 5, 6],
    [0, 4, 5, 0, 7],
    [0, 0, 6, 7, 0]
]

prim(graph)