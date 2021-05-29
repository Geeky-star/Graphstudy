
    def minSwaps(self, s: str) -> int:
        if len(s)==1:
            return 0

        count_0 = 0
        count_1 = 0
        
        for i in range(len(s)):
                if s[i] == '0':
                    count_0 += 1
                    
                else:
                    count_1 += 1
                    
        if abs(count_0 - count_1)>1:
            return -1
        
        
        s1 = ""
        s2 = ""
        for i in range(len(s)):
            if i%2==0:
                s1+="0"
                s2+="1"
                
            else:
                s2+="0"
                s1+="1"
                
        mis1 = 0
        mis2 = 0
        if count_0==count_1:
            for i in range(len(s)):
                if s[i]!=s1[i]:
                    mis1+=1
                    
                if s[i]!=s2[i]:
                    mis2+=1
            
            return min(mis1//2,mis2//2)
        
        if count_0>count_1:
            print(s1)
            
            for i in range(0,len(s)):
                if s[i]!=s1[i]:
                    mis1+=1
                    
            return mis1//2
        
        else:
            for i in range(0,len(s)):
                if s[i]!=s2[i]:
                    mis2+=1
                    
            return mis2//2
