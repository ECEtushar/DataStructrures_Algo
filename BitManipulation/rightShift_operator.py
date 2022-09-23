from bit_conversion import dec_to_bin, bin_to_dec

"""
Right shift operator shifts a binary number to right side by adding given number of 0s at the beginning 
"""

def rightShift(number:int, shift:int):
    if shift<=0:
        raise Exception("invalid limiter, limiter can't be lesser or equal to 0")
    
    bin_number = dec_to_bin(number)
    if shift >= len(bin_number):
        return 0
    bin_result = ("0"*shift)+bin_number
    bin_result = bin_result[0:len(bin_number)]
    print(bin_result)

    dec_result = bin_to_dec(bin_result)

    return dec_result



if __name__ == "__main__":
    num = 5
    shift = 9
    print(rightShift(num,shift))    
    inbuilt_rightShift = num >> shift # It is inbuilt bit_operator in python
    print(inbuilt_rightShift)
