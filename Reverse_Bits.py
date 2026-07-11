def reverseBits(n: int):
    string = f"{n:032b}"
    return int(string[::-1], 2)

if __name__ == "__main__":
    print(reverseBits(2147483644))