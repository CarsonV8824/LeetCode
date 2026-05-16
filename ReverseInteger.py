def reverse(x: int) -> int:
    sign = False
    if abs(x) != x:
        sign = True
    new_x = str(x)
    final = ""
    for i in range(len(new_x)-1, -1, -1):
        if sign and i == 0:
            break
        final += new_x[i]
    
    final = int(final)
    if sign:
        final *= -1
        if final < -1 * 2**31:
            return 0
        return final
    else:
        if final > 2**31 - 1:
            return 0
        return final
    
    
    
if __name__ == "__main__":
    print(reverse(-321))