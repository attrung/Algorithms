# python3

def parent(i):
    return int((i-1)/2)

def left(i):
    return 2*i + 1

def right(i):
    return 2*i + 2

def not_min(i, data):
    l = left(i)
    r = right(i)
    if l < len(data) and data[l] < data[i]:
        return True
    elif r < len(data) and data[r] < data[i]:
        return True
    else:
        return False

def shift_down(i, data, swaps):
    min_index = i
    l = left(i)
    if l < len(data) and data[l] < data[min_index]:
        min_index = l
    r = right(i)
    if r < len(data) and data[r] < data[min_index]:
        min_index = r
    if i != min_index:
        data[i], data[min_index] = data[min_index], data[i]
        swaps.append((i,min_index))
        return min_index

def pass_down(i, data, swaps):
    while not_min(i, data) == True:
        i = shift_down(i, data, swaps)

def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    for i in range(len(data) - 1, -1, -1):
        pass_down(i, data, swaps)
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
