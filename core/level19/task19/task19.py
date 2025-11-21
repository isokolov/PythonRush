# Максимальный поток в сети

# Есть нефтепровод (граф) заданный матрицей смежности.
# Число в матрице - это пропускная способность нефтепровода между двумя городами.
# Нужно подсчитать сколько максимально можно прокачать нефти между двумя вершинами.
# В теории графов: Найти максимальный поток в сети с источником и стоком.

# Подсказка 1:
# Используйте графовые алгоритмы, такие как алгоритм Форда-Фалкерсона, комбинированные с методами поиска в ширину (BFS) и в глубину (DFS).
# Подсказка 2:
# 1) Используйте BFS для поиска путей с доступным потоком.
# 2) Повторяйте процесс, пока существуют пути с доступным потоком.
# 3) Обновляйте резидуальные графы для учёта использованных потоков.


from collections import deque

def bfs(residual_graph, source, sink, parent):
    visited = [False] * len(residual_graph)
    queue = deque([source])
    visited[source] = True

    while queue:
        u = queue.popleft()

        for ind, val in enumerate(residual_graph[u]):
            if not visited[ind] and val > 0:
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u
                if ind == sink:
                    return True
    return False

def edmonds_karp(capacity_matrix, source, sink):
# Напишите тут ваш код


# Пример использования
capacity_matrix = [
    [0, 16, 13, 0, 0, 0],
    [0, 0, 10, 12, 0, 0],
    [0, 4, 0, 0, 14, 0],
    [0, 0, 9, 0, 0, 20],
    [0, 0, 0, 7, 0, 4],
    [0, 0, 0, 0, 0, 0]
]
source = 0
sink = 5

print("Максимальный поток: ", edmonds_karp(capacity_matrix, source, sink))
