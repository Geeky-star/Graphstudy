INF = 99999

graph = [[0, 5, INF, 10],
         [INF, 0, 3, INF],
         [INF, INF, 0,   1],
         [INF, INF, INF, 0]
         ]
         
v = 4


def printSolution(dist):
    
    for i in range(v):
        for j in range(v):
            if dist[i][j] == INF:
                print("INF")
                
            else:
                print(dist[i][j])
                
            if j==v-1:
                print(" ")

def floydWarshall(graph):
    
    dist = [[0 for i in range(v)] for j in range(v)]
    
    for i in range(v):
        for j in range(v):
            dist[i][j] = graph[i][j]
            
    for k in range(v):
        for i in range(v):
            for j in range(v):
                
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                
    printSolution(dist)
    
    
floydWarshall(graph)
