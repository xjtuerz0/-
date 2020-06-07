  # ------------------函数-------------------
def back_path(path,i,j,shortestPath):            #递归回溯
    print ("path[%s][%s] = "%(i,j),path[i][j])
    if -1 != path[i][j]:
        shortestPath = back_path(path,i,path[i][j],shortestPath)
        shortestPath = back_path(path,path[i][j],j,shortestPath)
    if j not in shortestPath:
        shortestPath.append(j)
    return shortestPath

def getShortestPath(graph,path,i,j):
    shortestPath = []
    dis = 0
    if graph[i][j] == float('inf') or i == j:
        print("顶点%s不能到达顶点%s！"%(i,j))
        return shortestPath
    elif path[i][j] == -1:
        shortestPath.append(i)
        shortestPath.append(j)
        dis+=graph[i][j]
    else :
        shortestPath.append(i)
        shortestPath = back_path(path,i,j,shortestPath)
        dis+=graph[i][j]
    print("V%s—>V%s: "%(i,j),shortestPath,"distance: ",dis)
    return shortestPath

def getAllShortestPath(graph,path):
    print("------正在生成全局最短路径------")
    ShortestPath_dict = {}
    for i in range(N):
        print("---------------",i,"-----------------")
        ShortestPath_dict[i] = {}
        for j in range(N):
            if i==j:
                continue
            
            else:
                # print("尝试生成顶点%s到顶点%s的最短路径..."%(i,j))

                shortestPath = getShortestPath(graph,path,i,j)
                ShortestPath_dict[i][j] = shortestPath
            # else :
            #     print("顶点重合")
        print("从%d出发到其余点的最佳路径为："%i,ShortestPath_dict[i])
    return ShortestPath_dict

# ----------------------定义--------------------
M=float('inf')      #无穷大

graph=[
    [0,5,M,7],\
    [M,0,4,2],\
    [3,3,0,2],\
    [M,M,1,0]
    ]
N = len(graph)
path = []
for i in range(N):
    path.append([])
    for j in range(N):
        path[i].append(-1)
print("Original Graph:")
for i in range(N):
    print(graph[i])

# -----------------Floyd Algorithm----------------
for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                path[i][j] = k
print("A")
for t in range(len(graph)):
    print(graph[t])
print("Path:")
for p  in range(N):
    print(path[p])

getAllShortestPath(graph,path)
# print("ShortestPath =\n",getAllShortestPath(graph,path))