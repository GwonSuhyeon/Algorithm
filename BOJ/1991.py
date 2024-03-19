def pre_order(parent):
    
    global right_node, left_node
    
    if parent == '.':
        return
    
    res.append(parent)
    pre_order(tree[parent][left_node])
    pre_order(tree[parent][right_node])

def in_order(parent):
    
    global right_node, left_node
    
    if parent == '.':
        return
    
    in_order(tree[parent][left_node])
    res.append(parent)
    in_order(tree[parent][right_node])

def post_order(parent):
    
    global right_node, left_node
    
    if parent == '.':
        return
    
    post_order(tree[parent][left_node])
    post_order(tree[parent][right_node])
    res.append(parent)

N = int(input())

global right_node, left_node
right_node = 1
left_node = 0

tree = {}
res = []

for i in range(N):
    root, left, right = input().split()
    tree[root] = [left, right]

res.clear()
pre_order('A')
print(''.join(res))

res.clear()
in_order('A')
print(''.join(res))

res.clear()
post_order('A')
print(''.join(res))