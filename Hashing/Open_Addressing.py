class OpenAd:
    def __init__(self,cap):
        self.cap=cap
        self.ht=['e']*cap
        self.currSz=0

    def hashFun(self,key):
        ind=key%self.cap
        return ind

    '<----Insert Function---->'
    def insert(self,x):
        if self.currSz<self.cap:
            idx=self.hashFun(x)
            if self.ht[idx]=='e' or self.ht[idx]=='d':
                self.ht[idx]=x
                self.currSz+=1
            else:
                nidx=idx+1
                while nidx!=idx:
                    if self.ht[nidx]=='e' or self.ht[nidx]=='d':
                        self.ht[nidx]=x
                        self.currSz+=1
                        return
                    if nidx==self.cap-1:
                        nidx=0
                    else:
                        nidx+=1
                return print('Hash Table is full!')
        else:
            return print('Hash Table is full!')

    def search(self,x):
        idx=self.hashFun(x)
        if self.ht[idx]==x:
            return print(True)
        else:
            nidx=idx+1
            hf=nidx%self.cap
            while hf!=idx:
                if self.ht[hf]==x:
                    return print(True)
                elif self.ht[hf]=='e':
                    return print(f'{x} not found')
                nidx+=1
                hf=nidx%self.cap

                
            return print(f'{x} not found')
                    

h=OpenAd(8)

print(f'Hash Table={h.ht} || Max Cap= {h.cap} || Current Size Of Table= {h.currSz}\n')#1
h.ht[5]='d'
h.insert(40)
h.insert(42)
h.insert(43)
h.insert(61)

print(f'Hash Table={h.ht} || Max Cap= {h.cap} || Current Size Of Table= {h.currSz}')#2
h.search(61)