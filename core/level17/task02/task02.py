# Поиск элемента в бинарном дереве

# Напишите функцию для поиска элемента в бинарном дереве поиска (BST).
# Функция должна принимать корневой узел дерева и значение искомого элемента
# и возвращать узел, содержащий искомое значение, или None, если элемент не найден.

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def search_bst(root: TreeNode, val: int) -> TreeNode:
# Напишите тут ваш код