
def rec_palin(string,i=0):
    if i>=len(string)//2:
        return True
    r=len(string)-1-i
    if string[i]!= string[r]:
        return False
    return rec_palin(string,i=i+1)



if __name__=="__main__":
    s= "abba"
    if rec_palin(s):
        print("Yes")
    else:
        print("No")