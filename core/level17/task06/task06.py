# Поиск пар чисел в AVL-дереве

# Напишите функции для нахождения минимального (find_min) и максимального (find_max) элемента в бинарном дереве поиска (BST).
# Функции должны принимать корневой узел дерева и возвращать узел с минимальным или максимальным значением.

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def find_min(node):
# Напишите тут ваш код

def find_max(node):
# Напишите тут ваш код

# Пример использования:
root = TreeNode(20)
root.left = TreeNode(10)
root.right = TreeNode(30)
root.left.left = TreeNode(5)
root.left.right = TreeNode(15)
root.right.right = TreeNode(35)

print("Минимальное значение:", find_min(root).val)
print("Максимальное значение:", find_max(root).val)