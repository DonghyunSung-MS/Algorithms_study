# i, j, cost
graph = [
    (1,2,13),
    (1,3,5),
    (2,4,9),
    (3,4,15),
    (3,5,3),
    (4,5,1),
    (4,6,7),
    (5,6,2)
]
graph.sort(key=lambda x:x[2], reverse=True) # cost 오름차순

mst = []
n = 6
p = [0]

for i in range(1,n+1):
    p.append(i)

def find(u):
    print(u)
    if u!=p[u]:
        p[u] = find(p[u])
    return p[u]

def union(u,v):
    root1 = find(u)
    root2 = find(v)
    p[root2] = root1



tree_edges = 0
mst_cost = 0
while True:
    if tree_edges==n-1:
        break
    u,v,wt = graph.pop()
    a = find(u)
    print(a, p)
    print("======================")
    b = find(v)
    print(a, p)
    print("======================")
    print("=+++++++++++++++++++++++++++")
    if a != b:

        union(u,v)
        mst.append((u,v))
        mst_cost += wt
        tree_edges += 1

print(mst)
print(mst_cost)