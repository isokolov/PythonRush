# Сортировка мусора

# Напишите функцию для упорядочения пакетов так, чтобы все зависимости были установлены перед установкой самого пакета.
# Используйте алгоритм топологической сортировки через поиск в глубину (DFS).
# Функция должна возвращать список пакетов в правильном порядке установки.


dependency_graph = dict()
visited = set()
temp_marked = set()
result = list()

def dfs(package):
    if package in temp_marked:
        raise ValueError("Cycle detected!")
    if package not in visited:
        temp_marked.add(package)
        for dep in dependency_graph.get(package, []):
            dfs(dep)
        temp_marked.remove(package)
        visited.add(package)
        result.append(package)

def topological_sort(packages):
# Напишите тут ваш код

# Example usage:
packages = [
    ('a', ['b', 'c']),
    ('b', ['c', 'd']),
    ('c', ['d']),
    ('d', [])
]

print(topological_sort(packages))
# Output: ['d', 'c', 'b', 'a']