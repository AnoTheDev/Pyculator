from array import array

# Adds two numbers in an array
def add (arr: array) -> int :
    out: int = 0
    for i in arr:
        if (int(i) == i):
            out += 1

    return out

