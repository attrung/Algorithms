# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])

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

def shift_down(i, data):
    min_index = i
    l = left(i)
    if l < len(data) and data[l] < data[min_index]:
        min_index = l
    r = right(i)
    if r < len(data) and data[r] < data[min_index]:
        min_index = r
    if i != min_index:
        data[i], data[min_index] = data[min_index], data[i]
        return min_index

def pass_down(i, data):
    while not_min(i, data) == True:
        i = shift_down(i, data)


def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    threads = []
    for i in range(n_workers):
        threads.append(i/n_workers)
    result = []
    for job in jobs:
        result.append(AssignedJob(int(round((threads[0] - int(threads[0]))*n_workers, 0)), int(threads[0])))
        threads[0] += job
        pass_down(0, threads)
    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
