def insHead(st,e):
    if st == []:
        st.append(e)
        return st
    x= st.pop()
    insHead(st,e)
    st.append(x)
    return st

def revStack(st):
    if st == [] or len(st) == 1:
        return st
    e = st.pop()
    revStack(st)
    insHead(st,e)
    return st


st = [1,2,3,4,5]
e= 0
insHead(st,e)
print('insHead: ',st)
st2 = [1,2]
revStack(st2)
print('revStack: ',st2)
