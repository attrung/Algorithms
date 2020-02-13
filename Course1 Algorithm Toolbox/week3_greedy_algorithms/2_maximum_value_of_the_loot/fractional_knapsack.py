# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0
    density = []
    for i in range(len(values)):
        density.append(values[i]/weights[i])
    index = sorted(range(len(density)),key = density.__getitem__)
    i = -1
    while capacity > 0 and abs(i)<=len(density):
        if capacity < weights[index[i]]:
            value += values[index[i]]*capacity/weights[index[i]]
            capacity = 0
        else:
            value += values[index[i]]
            capacity -= weights[index[i]]
        i -= 1
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
