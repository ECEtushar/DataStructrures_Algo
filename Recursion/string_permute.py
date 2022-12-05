class Solution:
    
    def permute(self,s, res, temp=''):
        if s=='':
            res.add(temp)
            return
        self.permute(s[1:], res, temp)
        self.permute(s[1:], res, temp+s[0])
    
    def swap(self,s,i,j):
        n=list(s)
        n[i],n[j] = n[j],n[i]
        return "".join(n)

    def permute2(self,s,res,n,i=0):
        if i==n:
            res.add(s)
            return
        for j in range(i,n):
            s=self.swap(s,i,j)
            self.permute2(s,res,n,i+1)
            s=self.swap(s,i,j)
        
    def solve(self,s,res):
        x=''
        for i in s:
            x+=i
            res.add(x)
        
    def checkInclusion(self, s1: str, s2: str) -> bool:
        res2 = set()
        res1 = set()
        self.permute(s2,res2)
        self.permute2(s1,res1,len(s1))
        print("res2= ",res2)
        print("res1= ",res1)
        for i in res1:
            if i in res2:
                return True
        
        return False
            
        

    

s=Solution()
print(s.checkInclusion("ab","eidbaooo"))
a="eidbaooo"
j=0
for i in range(0,10):
    print(a[i:i+2])
    j=i-1