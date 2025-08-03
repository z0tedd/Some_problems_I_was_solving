import heapq


def find_min_time_to_deliver(n, m, index, routes):
    # Создаем граф
    graph = {i: [] for i in range(n)}
    for start, end, time in routes:
        graph[start].append((end, time))
        graph[end].append((start, time))

    # Алгоритм Дейкстры
    distances = [float("inf")] * n
    distances[index] = 0
    priority_queue = [(0, index)]  # (время, вершина)

    while priority_queue:
        current_time, current_node = heapq.heappop(priority_queue)

        # Если уже обработали вершину, пропускаем
        if current_time > distances[current_node]:
            continue

        # Обновляем расстояния до соседей
        for neighbor, travel_time in graph[current_node]:
            new_time = current_time + travel_time
            if new_time < distances[neighbor]:
                distances[neighbor] = new_time
                heapq.heappush(priority_queue, (new_time, neighbor))

    # Проверяем достижимость всех деревень
    max_time = max(distances)
    return -1 if max_time == float("inf") else max_time


# Входные данные
n, m = map(int, input().split())
index = int(input())
routes = [list(map(int, input().split())) for i in range(m)]

# Вывод результата
result = find_min_time_to_deliver(n, m, index, routes)
print(result)
