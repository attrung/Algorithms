# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    m1 = 0
    for i in range(0,n):
        if numbers[i] > numbers[m1]:
            m1 = i
    
    if m1 == 0:
        m2 = 1
    else:
        m2 = 0
    
    for i in range(0,n):
        if numbers[i] > numbers[m2] and i != m1:
            m2 = i
    return numbers[m1]*numbers[m2]


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
