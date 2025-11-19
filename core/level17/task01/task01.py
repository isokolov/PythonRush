# Бинарное дерево

# Напишите функцию для вставки нового элемента в бинарное дерево поиска (BST).
# Функция должна принимать корневой узел дерева и значение нового элемента и возвращать обновленное дерево.

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def insert_into_bst(root, value):
    # Напишите тут ваш код

    return root