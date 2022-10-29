def delK(st,k):
    if k == 1:
        st.pop()
        return st
    x = st.pop()
    delK(st,k-1)
    st.append(x)
    return st

def delMiddle(st):
    if st==[] or len(st)==1:
        return st
    
    k = len(st)//2
    delK(st,k+1)
    
    return st


st = [1,2,3,4,5]
delMiddle(st)
print(st)