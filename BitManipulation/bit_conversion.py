
# function for converting decimal to binary
def dec_to_bin(n):
    binary = ""
    
    while n!=1:
        rem = n%2
        quot = n//2
        binary+=str(rem)
        n=quot

    binary+="1"
    return binary[::-1]

# function for converting binary to decimal
def bin_to_dec(bin):
    bin_set = {"1","0"}

    bin = bin[::-1]
    
    for i in bin:
        if i not in bin_set:
            return "invalid binary number"

    decimal = 0

    for i in range(len(bin)):
        decimal += int(bin[i])*(2**i)

    return decimal


if __name__ == "__main__":
    n = 13
    bin = "1010101"
    print(bin_to_dec(bin))
    print(dec_to_bin(n))