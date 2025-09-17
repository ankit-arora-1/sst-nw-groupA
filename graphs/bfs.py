from collections import deque


def bfs(graph, start_vertex):
    visited = set()
    queue = deque()

    queue.append(start_vertex)
    visited.add(start_vertex)

    bfs_travel = []
    while len(queue) > 0:
        current_vertex = queue.popleft()
        bfs_travel.append(current_vertex)

        print(f"visited vertex: {current_vertex}")

        neighbours = graph[current_vertex]
        for neighbour in neighbours:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

    return bfs_travel


def main():

    graph = {}
    graph[1] = [2, 3]
    graph[2] = [4, 5]
    graph[3] = [5]
    graph[4] = [6]
