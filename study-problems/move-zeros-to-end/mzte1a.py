def moveZerosToEnd(arr):
    results = list()
    zeros = list()
    for n in arr:
        if n != 0:
            results.append(n)
        else:
            zeros.append(0)
    return results + zeros
