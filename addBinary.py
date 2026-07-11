# this solution is in the 100% index for speed!

def addBinary(a: str, b: str) -> str:
    first = int(a, 2)
    second = int(b, 2)
    print(first, second)
    return f"{first + second:b}"

if __name__ == "__main__":
    print(addBinary("11", "1"))