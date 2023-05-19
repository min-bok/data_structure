tree = ["A", "B", "C", "D", "E", "F", None, "G"]

# 자식 노드 찿기
# i = 0
# n = len(tree)
# while i < n:
#     if tree[i]:
#         print(f"parent: {tree[i]}", end=", ")
#         left = 2 * i + 1
#         right = left + 1
#         if left < n and tree[left] is not None:
#             print(f"left: {tree[left]}", end=", ")
#         if right < n and tree[right] is not None:
#             print(f"right: {tree[right]}", end=", ")
#         print()
#     i += 1

# parent: A, left: B, right: C, 
# parent: B, left: D, right: E,
# parent: C, left: F,
# parent: D, left: G,
# parent: E,
# parent: F,
# parent: G,

# 부모 노드 찾기
# n = len(tree)
# i = n-1
# while i > 0:
#     if tree[i]:
#         print(f"parent of {tree[i]} => {tree[(i-1)//2]}")
#     i -= 1

# parent of G => D
# parent of F => C
# parent of E => B
# parent of D => B
# parent of C => A
# parent of B => A

# 재귀 순회 함수 만들기
tree = ["A", "B", "C", "D", "E", "F", None, "G"]

## 전위 순회
# def preorder(tree, i=0):
#     if i < len(tree):
#         print(tree[i], end=" ")
#         left = 2 * i + 1
#         right = left + 1
#         if left < len(tree) and tree[left] is not None:
#             preorder(tree, left)
#         if right < len(tree) and tree[right] is not None:
#             preorder(tree, right)

# preorder(tree) # A B D G E C F

## 방문 결과를 리스트로 반환
# def preorder(tree, i=0): 
#     if i < len(tree):
#         result = [tree[i]]
#         left = 2 * i + 1 
#         right = left + 1 
#         if left < len(tree) and tree[left] is not None:
#             result += preorder(tree, left)
#         if right < len(tree) and tree[right] is not None:
#             result += preorder(tree, right) 
#         return result
    
# print(preorder(tree)) # ['A', 'B', 'D', 'G', 'E', 'C', 'F']

# def preorder(tree):  
#     def _preorder(tree, i = 0):
#         if i < len(tree):
#             res.append(tree[i])
#             left = 2 * i + 1
#             right = left + 1    
#             if left < len(tree) and tree[left is not None]:
#                 _preorder(tree, left)
#             if right < len(tree) and tree[right is not None]:
#                 _preorder(tree, right)          
#     res = []    
#     _preorder(tree)
#     return res

## 간단하게
# def preorder(tree):  
#     def _preorder(tree, i = 0):
#         if i >= len(tree) or tree[i] is None: #인덱스를 벗어나거나, 원소가 None이면 종료
#             return
#         res.append(tree[i])
#         left = 2 * i + 1
#         right = left + 1    
#         _preorder(tree, left)
#         _preorder(tree, right)

#     res = []    
#     _preorder(tree)
#     return res

## 중위순회
# def inorder(tree):
#     def _inorder(tree, i = 0):
#         if i >= len(tree) or tree[i] is None:
#             return
#         left = 2 * i + 1
#         right = left + 1
#         _inorder(tree, left)
#         res.append(tree[i])
#         _inorder(tree, right)

#     res = []    
#     _inorder(tree)
#     return res

# print(inorder(tree)) # ['G', 'D', 'B', 'E', 'A', 'F', 'C']

## 후위순회
# def postorder(tree):
#     def _postorder(tree, i = 0):
#         if i >= len(tree) or tree[i] is None:
#             return
#         left = 2 * i + 1
#         right = left + 1
#         _postorder(tree, left)
#         _postorder(tree, right)
#         res.append(tree[i])

#     res = []    
#     _postorder(tree)
#     return res

# print(postorder(tree)) # ['G', 'D', 'E', 'B', 'F', 'C', 'A']

## 스택으로 순회 함수 만들기
## 전위순회
# def preorder(tree):
#     if not tree:
#         return []
#     res, stack = [], [0]
    
#     while stack:
#         parent = stack.pop()
#         res.append(tree[parent])
#         left = 2 * parent + 1
#         right = left + 1
#         if right < len(tree) and tree[right] is not None:
#             stack.append(right)
#         if left < len(tree) and tree[left] is not None:
#             stack.append(left)
#     return res

# print(preorder(tree)) # ['A', 'B', 'D', 'G', 'E', 'C', 'F']

# def preorder(tree):
#     if not tree:
#         return []
#     res, stack = [], [0]

#     while stack:
#         index = stack.pop()
#         res.append(tree[index])
#         index = 2 * index + 2
#         if index < len(tree) and tree[index] is not None:
#             stack.append(index)
#         index -= 1
#         if index < len(tree) and tree[index] is not None:
#             stack.append(index)
#     return res

## 중위순회
# def inorder(tree):
#     if not tree:
#         return []
#     index = 0
#     res, stack = [], []

#     while True:
#         if index < len(tree) and tree[index] is not None:
#             stack.append(index)
#             index = 2 * index + 1
#         elif stack:
#             index = stack.pop()
#             res.append(tree[index])
#             index = 2 * index + 2
#         else: 
#             break
#     return res

# print(inorder(tree)) # ['G', 'D', 'B', 'E', 'A', 'F', 'C']

## 후위순회
# def postorder(tree):
#     if not tree:
#         return []
#     res, stack = [], [0]
#     visit_order = []
#     # visit_order = [0, 2, 5, 1, 4, 3, 7]
#     # stack = [] 
#     #  tree = ["A", "B", "C", "D", "E", "F", None, "G"]

#     while stack:
#         index = stack.pop()
#         visit_order.append(index)
#         index = 2 * index + 1 
#         if index < len(tree) and tree[index] is not None:
#             stack.append(index)
#         index = index + 1
#         if index < len(tree) and tree[index] is not None:
#             stack.append(index)
    
#     # print(stack)
#     print(visit_order)

#     while visit_order:
#         index = visit_order.pop()
#         res.append(tree[index])
#         print(res)
#     return res

# print(postorder(tree)) # ['G', 'D', 'E', 'B', 'F', 'C', 'A']

## 레벨 순서 순회
# def levelorder(tree):
#     if not tree:
#         return []
#     res, queue = [], [0]

#     while queue:
#         index = queue.pop(0)
#         res.append(tree[index])
#         index = 2 * index + 1
#         if index < len(tree) and tree[index] is not None:
#             queue.append(index)
#         index += 1
#         if index < len(tree) and tree[index] is not None:
#             queue.append(index)
#     return res
# ['A', 'B', 'C', 'D', 'E', 'F', 'G']

# 연결리스트
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

# class Tree:
#     def __init__(self, node=None):
#         self.root = node

# if __name__ == "__main__":
#     tree = Tree(Node("A"))
#     tree.root.left = Node("B")
#     tree.root.right = Node("C")
#     tree.root.left.left = Node("D")
#     tree.root.left.right = Node("E")
#     tree.root.right.left = Node("F")
#     tree.root.left.left.left = Node("G")

# print(tree.root.data) # 

## 재귀 순회 함수
## 전위 순회
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self, node=None):
        self.root = node

    def preorder(self):
        def _preorder(node): 
            if node is None:
                return
            res.append(node.data)
            _preorder(node.left)
            _preorder(node.right)

        res = []
        _preorder(self.root)
        return res

if __name__ == "__main__":
    tree = Tree(Node("A"))
    tree.root.left = Node("B")
    tree.root.right = Node("C")
    tree.root.left.left = Node("D")
    tree.root.left.right = Node("E")
    tree.root.right.left = Node("F")
    tree.root.left.left.left = Node("G")

    print(tree.preorder()) # 전위순회: ['A', 'B', 'D', 'G', 'E', 'C', 'F']

