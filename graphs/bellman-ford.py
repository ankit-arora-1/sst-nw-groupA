import math


def bellman_ford(graph, start):
    distances = {}
    for vertex in graph:
        distances[vertex] = math.inf

    distances[start] = 0

    for iteration in range(len(graph) - 1):
        for vertex in graph:
            for neighbour, weight in graph[vertex]:
                new_distance = distances[vertex] + weight

                if new_distance < distances[neighbour]:
                    distances[neighbour] = new_distance

    has_negative_cycle = False
    for vertex in graph:
        for neighbour, weight in graph[vertex]:
            new_distance = distances[vertex] + weight
            if new_distance < distances[neighbour]:
                has_negative_cycle = True

    return distances, has_negative_cycle
