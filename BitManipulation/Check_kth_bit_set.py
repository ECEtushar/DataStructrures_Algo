from bit_conversion import bin_to_dec, dec_to_bin


def kth_bit(n,k) -> str:
    if n==0:
        return False
    bin_num = dec_to_bin(n)
    l = len(bin_num)
    if k > l:
        return False

    if bin_num[l-(k)] == "1":
        return True
    return False

if __name__ == "__main__":
    n=5
    k=1
    print(kth_bit(n,k))