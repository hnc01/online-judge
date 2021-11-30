class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraveralHelper(self, root, result):
    if root is not None:
        if root.left is not None:
            self.inorderTraveralHelper(root.left, result)

        result.append(root.val)

        if root.right is not None:
            self.inorderTraveralHelper(root.right, result)


def inorderTraversal(self, root: TreeNode) -> list[int]:
    result = []

    self.inorderTraveralHelper(root, result)

    return result
