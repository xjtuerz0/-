from collections import defaultdict
from heapq import *

def dijkstra(graph_dict, from_node, to_node):
    cost = -1
    Shortest_path=[]
    q, seen = [(0,from_node,())], set()
    while q:
        (cost,v1,path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == to_node: # Find the to_node!!!
                break;
            for v2,c in graph_dict.get(v1, ()):
                if v2 not in seen:
                    heappush(q, (cost+c, v2, path))

    # Check the way to quit 'while' loop
    if v1 != to_node:
        # IF there isn't a path from from_node to to_node, THEN return null!!!
        print("node: %s cannot reach node: %s" %(from_node,to_node))
        cost = -1
        Shortest_path=[]
        return cost,Shortest_path
    else:
        # IF there is a path from from_node to to_node, THEN format the path and return!!!
        left = path[0]
        Shortest_path.append(left)
        right = path[1]
        while len(right)>0:
            left = right[0]
            Shortest_path.append(left)
            right = right[1]
        Shortest_path.reverse()
        
    return cost,Shortest_path

def dijkstra_all(graph_dict):
    Shortest_path_dict = defaultdict(dict)
    for i in nodes:
        print("from",i)
        for j in nodes:
            if i != j:
                cost,Shortest_path = dijkstra(graph_dict,i,j)
                Shortest_path_dict[i][j] = Shortest_path
                print("To", j,  "cost", cost,"Shortest_path",Shortest_path)  
    return Shortest_path_dict

nodes=['A','B','C','D','E']
print("nodes =",nodes)
M=float("inf")
# Describing graph by 2-D list
graph_list = [ 
[0,6,M,1,M],  
[6,0,5,2,2],  
[M,5,0,M,5],  
[1,2,M,0,1],  
[M,2,5,1,0]
]
print("graph_list = [")
for l in graph_list:
    print(str(l)+",")
print("]\n")

# Describing graph by a list of tuple
graph_edges = []
print ("graph_edges = [")
for i in nodes:
    for j in nodes:
        if i!=j and graph_list[nodes.index(i)][nodes.index(j)]!=M:
            graph_edges.append((i,j,graph_list[nodes.index(i)][nodes.index(j)]))
            print (str((i,j,graph_list[nodes.index(i)][nodes.index(j)]))+", ",end="")
    print()
print("]\n")

# Describing graph by dict
graph_dict = defaultdict(list)
print("graph_dict = {")
for tail,head,cost in graph_edges:
    graph_dict[tail].append((head,cost))
for key in graph_dict:
    print("'%s': %s" %(key, graph_dict[key]))
print("}\n")

# 
#from_node = input ("Please input the from_node =  ")
#to_node = input("Please input the to_node = ")
#cost,Shortest_path = dijkstra(graph_dict, from_node, to_node)
#print ('The shortest path = %s, cost = %s'%(Shortest_path,cost))
print ("----------------Dijkstra----------------")
Shortest_path_dict = dijkstra_all(graph_dict)
""""
print("Shortest_path_dict = {")
for key in Shortest_path_dict:
    print("'%s': %s," %(key, Shortest_path_dict[key]))
print("}")
"""