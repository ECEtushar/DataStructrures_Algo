from bit_conversion import dec_to_bin, bin_to_dec

"""
Left shift operator shifts the binary number to left with given values following by 0s
"""

def leftShift(number:int, limiter:int):
    if limiter<=0:
        raise Exception("invalid limiter, limiter can't be lesser or equal to 0")
    shift = "0"*limiter
    bin_number = dec_to_bin(number)
    bin_result = bin_number+shift

    dec_result = bin_to_dec(bin_result)

    return dec_result




if __name__ == "__main__":
    num = 5
    shift = 1
    print(leftShift(num,shift))
    inbuilt_leftShift = num << shift # It is inbuilt bit_operator in python
    print(inbuilt_leftShift)
