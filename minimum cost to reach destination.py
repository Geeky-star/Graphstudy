#Minimum cost to reach destination from train in directed acyclic graph

INF = 2147483647
n = 4 

def minCost(cost):
    dist = [INF]*n
    dist[0] = 0
    
    for i in range(n):
        for j in range(i+1,n):
            if dist[j] > dist[i] + cost[i][j]:
                dist[j] = dist[i] + cost[i][j]
                
    return dist[n-1]
    
cost= [ [0, 15, 80, 90],
            [INF, 0, 40, 50],
            [INF, INF, 0, 70],
            [INF, INF, INF, 0]]
             
print(minCost(cost))
