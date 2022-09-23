from bit_conversion import bin_to_dec, dec_to_bin

"""
In AND, the output will be "1" only when both the input bits are "1" else "0" 
"""

def bitwise_and(x,y):
    bin_x = dec_to_bin(x)
    bin_y = dec_to_bin(y)
    

    len_x = len(bin_x)
    len_y = len(bin_y)
    diff = abs(len_x-len_y)
    
    if len_x>len_y:
        bin_y = ("0"*diff)+bin_y

    elif len_x<len_y:
        bin_x = ("0"*diff)+bin_x


    bin_res = ''
    n = len(bin_x)
    i=0
    while i<n:
        bin_res+=str(int(bin_x[i])*int(bin_y[i]))
        i+=1
    print(bin_res)
    return bin_to_dec(bin_res)


if __name__ == "__main__":
    print(bitwise_and(85,2))

