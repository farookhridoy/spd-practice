# Binary Search Tree
class Node:
    def __init__(self, key) -> None:
        self.left = None
        self.right = None
        self.val = key

    # Traversing in order
    # inorder = (left,root,right)
    def in_order(self):
        if self.left:
            self.left.in_order()
        print(self.val, end=' ')
        if self.right:
            self.right.in_order()

    # Traversing on pre-order
    # preorder = (root,left(left side preorder),right(right side preorder))

    def pre_order(self):
        print(self.val, end=' ')
        if self.left:
            self.left.pre_order()
        if self.right:
            self.right.pre_order()

    # Traversing post order
    # post order = (left, right, root)

    def post_order(self):
        if self.left:
            self.left.post_order()
        if self.right:
            self.right.post_order()

        print(self.val, end=' ')


# Initial node
root = Node(1)
root.left = Node(2)
root.left.left = Node(12)
root.left.right = Node(15)
root.right = Node(3)
root.right.left = Node(7)

print("\nIn order Traversal: ", end="")
root.in_order()

print("Pre order Traversal: ", end="")
root.pre_order()

print("\nPost in order Traversal: ", end="")
root.post_order()
