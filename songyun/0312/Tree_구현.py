class Node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

# 전위 순회
def pre_order(node):
    print(node.data, end=' ')
    if node.left_node != None:
        pre_order(tree[node.left_node])
    if node.right_node != None:
        pre_order(tree[node.right_node])

# 중위 순회
def in_order(node):
    if node.left_node != None:
        in_order(tree[node.left_node])
    print(node.data, end=' ')
    if node.right_node != None:
        in_order(tree[node.right_node])

# 후위 순회
def post_order(node):
    if node.left_node != None:
        post_order(tree[node.left_node])
    if node.right_node != None:
        post_order(tree[node.right_node])
    print(node.data, end= ' ')

# 노드의 갯수
n = int(input())
tree = {}

for i in range(n):
    # data = 본인 노드, left_node = 왼쪽 자식, right_node = 오른쪽 자식
    data, left_node, right_node = input().split()

    # 자식이 없는 노드의 경우
    if left_node == "None":
        left_node = None
    if right_node == "None":
        right_node = None
    tree[data] = Node(data, left_node, right_node)


pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])


# 입력예시
# 7
# A B C
# B D E
# C F G
# D None None
# E None None
# F None None
# G None None

# 출력
# A B D E C F G
# D B E A F C G
# D E B F G C A

