# python3
import sys


def compute_min_refills(distance, tank, stops):
    now = 0
    count = 0
    stops.append(distance)
    for i in range(len(stops)):
        if now + tank >= distance:
            return count
        else:
            if stops[i] <= now + tank < stops[i+1]:
                count += 1
                now = stops[i]
    return -1



if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
