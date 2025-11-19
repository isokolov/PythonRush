# Поиск в AVL-дереве

# Напишите функцию search для поиска элемента в бинарном дереве поиска (BST).
# Функция должна принимать корневой узел дерева и значение искомого элемента и возвращать узел,
# содержащий искомое значение, или None, если элемент не найден.

class TreeNode:
    def __init__(self, key, left=None, right=None, height=1):
        self.key = key
        self.left = left
        self.right = right
        self.height = height

def search(root, key):
# Напишите тут ваш код


# Пример использования:
# root = TreeNode(10)
# root.left = TreeNode(5)
# root.right = TreeNode(15)
# result = search(root, 15)
# print(result.key if result else "Not found")