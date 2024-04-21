'''
BINARY TREE 
-----------
- EACH NODE HAS 2 CHILDREN (MAX)
- LEFT CHILD OF BINARY TREE SHOULD BE SMALLER THAN RIGHT CHILD

- REFERENCE: https://www.youtube.com/watch?v=TezryjBe3Ts&list=PLMz1vLpcJgGDeVDybqQeZ0EewZcRF_1m_
'''

# DEFINING A TREE

class Node: # NODE HAS 3 ITEMS (LEFT, RIGHT CHILD, DATA (PARENT))
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

# DEFINING AN INSERT FUNCTION

    def insert(self, data):
        if self.data is None:
            self.data = data
        else:
            if data < self.data: # ADDING TO THE LEFT SUBTREE
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data) # RECURSIVELY INSERT DATA TO THE LEFT SUBTREE
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
    
def inOrderPrint(root): # RUNS RECURSIVELY
    if root is None: # IF THIS PART IS NOT THERE, IT GIVES AN ERROR (TRY AND SEE!)
        return
    inOrderPrint(root.left) # LEFT
    print(root.data, end = " ") # ROOT 
    inOrderPrint(root.right) # RIGHT

def preOrderPrint(root):
    if root is None:
        return
    print(root.data, end = " ") # ROOT
    preOrderPrint(root.left) # LEFT
    preOrderPrint(root.right) # RIGHT

def postOrderPrint(root):
    if root is None:
        return
    preOrderPrint(root.left) # LEFT
    preOrderPrint(root.right) # RIGHT
    print(root.data, end = " ") # ROOT

from collections import deque # IMPORTING 'DOUBLY ENDED QUEUE' (BUT WE USING IT AS A NORMAL QUEUE, FOR BFS)

def bfs(root):
    if root is None:
        return
    queue = deque() # CREATES A QUEUE TO STORE THE NODES
    queue.append(root)

    while queue:
        node = queue.popleft() # DEQUEUE THE FRONT NODE
        print(node.data, end = " ")
        if node.left: # ENQUEUE LEFT CHILD IF IT EXISTS
            queue.append(node.left)
        if node.right: # ENQUEUE RIGHT CHILD IF IT EXISTS
            queue.append(node.right)

if __name__ == '__main__':
    root = Node('g') # INSERTING ALL THE NODES INTO THE TREE
    root.insert('c')
    root.insert('b')
    root.insert('a')
    root.insert('e')
    root.insert('d')
    root.insert('f')
    root.insert('i')
    root.insert('h')
    root.insert('j')
    root.insert('k')

# PRINTING ALL NODES IN DFS - DEPTH FIRST SEARCH (STACK)
# DFS IS OF 3 TYPES -> PREORDER, INORDER, POSTORDER

# PRINTING ALL NODES IN INORDER TRAVERSAL (LEFT-ROOT-RIGHT)

print("DFS -> InOrder Traversal: ")
inOrderPrint(root)
print("\n")

# PRINTING ALL NODES IN PREORDER TRAVERSAL (ROOT-LEFT-RIGHT) [REGULAR DFS]

print("DFS (REGULAR) -> PreOrder Traversal:")
preOrderPrint(root)
print("\n")

# PRINTING ALL NODES IN POSTORDER TRAVERSAL (LEFT-RIGHT-ROOT)

print("DFS -> PostOrder Traversal:")
postOrderPrint(root)
print("\n")

# PRINTING ALL NODES IN BFS - BREADTH FIRST SEARCH (QUEUE)

print("BFS -> Breadth First Search:")
bfs(root)
print("\n")
