tree = ["A", "B", "C", "D", "E", "F", None, "G"]

# 자식 노드 찿기
i = 0
n = len(tree)
while i < n:
    if tree[i]:
        print(f"parent: {tree[i]}", end=", ")
        left = 2 * i + 1
        right = left + 1
        if left < n and tree[left] is not None:
            print(f"left: {tree[left]}", end=", ")
        if right < n and tree[right] is not None:
            print(f"right: {tree[right]}", end=", ")
        print()
    i += 1

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