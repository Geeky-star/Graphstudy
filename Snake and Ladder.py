def minThrow(self, N, arr):
        ladder = [-1]*30
        snake = [-1]*30
        for i in range(N//2):
            ladder[arr[2*i]] = arr[2*i+1]
        
        for j in range(N//2,N):
            snake[arr[2*j]] = arr[2*j+1]
            
        visited = [False]*31
        
        q = []
        q.append(1)
        found = False
        mov = 0
        while q and found==False:
            
            sz = len(q)
            
            while sz:
                t = q.pop(0)
                for dist in range(1,7):
                    if t + dist == 30:
                        found = True
                        break
            
                    if t+dist<=30 and visited[t+dist] == False:
                      if ladder[t+dist]!=-1:
                       ve = ladder[t+dist]
                       visited[ladder[ve]] = True
                       
                       if ve==30:
                           found = True
                           break
                
                      elif snake[t+dist]!=-1:
                       ve = snake[t+dist]
                       visited[snake[t+dist]] = True
                       if ve==30:
                           found=True
                           break
                  
                
                      elif visited[t+dist] == False and snake[t+dist]==-1 and ladder[t+dist]==-1:
                          ve = t+dist
                          visited[t+dist] = True
                    
                    q.append(ve)
                  
                sz-=1
            
            mov+=1
        
        if found==True:    
            return mov
        
        else:
            return -1
            
