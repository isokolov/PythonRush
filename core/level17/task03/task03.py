# AVL-дерево

# Напишите функцию для вставки нового элемента в AVL-дерево.
# Напишите функции get_height, update_height, left_rotate и right_rotate

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def get_height(node):
# Напишите тут ваш код

def update_height(node):
# Напишите тут ваш код

def left_rotate(z):
# Напишите тут ваш код

def right_rotate(z):
# Напишите тут ваш код

def get_balance(node):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)

def insert(root, key):
    if not root:
        return TreeNode(key)
    elif key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    update_height(root)

    balance = get_balance(root)

    # Left Left Case
    if balance > 1 and key < root.left.key:
        return right_rotate(root)

    # Right Right Case
    if balance < -1 and key > root.right.key:
        return left_rotate(root)

    # Left Right Case
    if balance > 1 and key > root.left.key:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    # Right Left Case
    if balance < -1 and key < root.right.key:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root