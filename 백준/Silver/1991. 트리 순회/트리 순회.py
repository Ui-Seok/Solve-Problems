import sys
input = sys.stdin.readline

n = int(input())

graph = {}
for _ in range(n):
    a, b, c = input().split()
    graph[a] = [b, c]

def preorder(x):
    if x != ".":
        print(x, end = "")
        preorder(graph[x][0])
        preorder(graph[x][1])

def inorder(x):
    if x != ".":
        inorder(graph[x][0])
        print(x, end = "")
        inorder(graph[x][1])

def postorder(x):
    if x != ".":
        postorder(graph[x][0])
        postorder(graph[x][1])
        print(x, end = "")

preorder("A")
print()
inorder("A")
print()
postorder("A")