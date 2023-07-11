from sys import maxsize
from itertools import permutations
V = 4
def tsp(graph,s):
    vertex = []
    for i in range(V):
        if 1!=s:
            vertex.append(i)
    min_path=maxsize
    next_permutation=permutations(vertex)
    for i in next_permutation:
        current_pathweight=0
        k=s
        for j in i:
            current_pathweight+=graph[k][j]
            k=j
        current_pathweight+=[k][s]
        min_path=min(min_path,current_pathweight)
    return min_path
if __name__ == "__main__":
    graph=[[0,20,10,12],[20,0,15,11],
           [10,15,0,17],[12,11,17,0]]
    s=0
    print(tsp(graph,s))