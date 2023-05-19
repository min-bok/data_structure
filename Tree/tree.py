# tree = [5,2,6,1,4]
# 이진 트리 구현
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, data):
        self.root = Node(data)
        self.count = 1

    def __len__(self):
        return self.count
    
    def insert(self, data):
        newNode = Node(data)
        currentNode = self.root

        while currentNode:
            if data == currentNode.data:
                return
            elif data < currentNode.data:
                if not currentNode.left:
                    currentNode.left = newNode
                    self.count += 1
                    return
                else:
                    currentNode = currentNode.left
            elif data > currentNode.data:
                if not currentNode.right:
                    currentNode.right = newNode
                    self.count += 1
                    return
                else:
                    currentNode = currentNode.right

    # 구현하고싶은것
    # 전위순회, 중위순회, 후회순회
    # 노드 깊이
    # 노드 삭제
    # 노드 존재 여부

t = BinaryTree(5)
t.insert(2)
t.insert(6)
t.insert(1)
t.insert(4)

print(t.root.left.left.data)