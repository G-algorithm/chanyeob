class Node:
    def __init__(self,item,left,right):
        self.item = item
        self.left = left
        self.right = right


def preorder(node):
    # m, l, r
    '''
    :param node: Node
    :return: str
    '''
    print(node.item,end="")
    if node.left != '.':
        preorder(tree[node.left])
    if node.right != '.':
        preorder(tree[node.right])




def inorder(node):
    # l, m, r
    '''
    :param node: Node
    :return: None
    '''
    if node.left != '.':
        inorder(tree[node.left])
    print(node.item,end="")
    if node.right != '.':
        inorder(tree[node.right])


def postorder(node):
    # l, r, m
    '''
    :param node: Node
    :return: str
    '''
    if node.left != '.':
        postorder(tree[node.left])
    if node.right != '.':
        postorder(tree[node.right])
    print(node.item,end="")

N = int(input())
tree = {}


for _ in range (N):
    m,l,r = input().split()
    tree[m] = Node(m,l,r)

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])