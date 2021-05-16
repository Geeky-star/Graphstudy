import queue
import math 

def isPossible(m, n, k, r, X, Y):
        
        rect = [[0]*n for i in range(m)]
        
        for i in range(m):
          for j in range(n):
            for p in range(k):
                if(math.sqrt((pow((X[p] - 1 - i), 2) + pow((Y[p] - 1 - j), 2))) <= r):
                    rect[i][j] = -1
                    
        if rect[0][0] == -1:
            return False
            
            
            
        q = queue.Queue()
        
        rect[0][0] = 1
        q.put([0,0])
        
        while not q.empty():
            
            arr = q.get()
            x = arr[0]
            y = arr[1]
            
            if x>0 and y>0 and rect[x-1][y-1]==0:
                
                rect[x-1][y-1] = 1
                v = [x-1,y-1]
                q.put(v)
                
            elif x>0 and rect[x-1][y] == 0:
                rect[x-1][y] = 1
                q.put([x-1,y])
                
            elif y<n-1 and x > 0 and rect[x-1][y+1] == 0:
                
                rect[x-1][y+1] = 1
                q.put([x-1,y+1])
                
            elif y>0 and rect[x][y-1]==0:
                rect[x][y-1]=1
                q.put([x,y-1])
                
            elif y<n-1 and rect[x][y+1]==0:
                rect[x][y+1] = 1
                q.put([x,y+1])
                
                
            elif x<m-1 and y>0 and rect[x+1][y-1]==0:
                rect[x+1][y-1]=1
                q.put([x+1,y-1])
                
                
            elif x<m-1 and rect[x+1][y] == 0:
                rect[x+1][y] = 1
                q.put([x+1,y])
                
            elif x<m-1 and y<n-1 and rect[x+1][y+1]==0:
                rect[x+1][y+1]=1
                q.put([x+1,y+1])
                
                
            return (rect[m-1][n-1] == 1)

m1 = 5
n1 = 5
k1 = 2
r1 = 1
X1 = [1, 3]
Y1 = [3, 3]
     
    # Function call
if (isPossible(m1, n1, k1, r1, X1, Y1))==True:
    print("Possible")
else:
    print("Not Possible")                
                
         
