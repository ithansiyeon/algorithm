class Node:
    def __init__(self,node,left,right):
        self.left = left
        self.right = right
        self.data = node

def preorder(node):
    print(node.data,end='')
    if node.left !='.':
        preorder(tree[node.left])
    if node.right !='.':
        preorder(tree[node.right])

def postorder(node):
    if node.left !='.':
        postorder(tree[node.left])
    if node.right !='.':
        postorder(tree[node.right])
    print(node.data,end='')

def inorder(node):
    if node.left !='.':
        inorder(tree[node.left])
    print(node.data,end='')
    if node.right !='.':
        inorder(tree[node.right])

n = int(input())
tree= {}
for i in range(n):
    node,left,right = input().split(" ")
    tree[node] = Node(node=node,left=left,right=right)

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])



