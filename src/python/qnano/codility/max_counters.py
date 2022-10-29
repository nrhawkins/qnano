def solution(N, A):

    counters = [0] * N
    current_max = 0
    last_max = 0

    for a in A:
        if a != N+1:
            counters[a-1] = max(counters[a-1], last_max)
            counters[a-1] += 1
            current_max = max(current_max, counters[a-1])
        else:
            last_max = current_max

    for i in range(N):
        counters[i] = max(counters[i], last_max)

    return counters






A = [3, 4, 4, 6, 1, 4, 4]
N = 5
print(solution(N, A))
assert solution(N, A) == [3, 2, 2, 4, 2]