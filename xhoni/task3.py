# Task 3: Focus on efficiency
# A = [N*int, int(S)]
# Count number of CONTINUOUS fragments of A that has mean equal to S
# If S > 1B, return 1B

# E.g.
# A = [2,1,3] S=2 should return 3, because mean(2), mean(1,3) and mean(2,1,3) are all =2=S
# A = [0,4,3,-1] S=2 should return 2, because mean(0,4) and mean(4,3,-1) are all =2=S
# A = [2,1,4] S=3 should return 0, because no sublist can have mean of 3

# len(A) < 100,000
# S in [-1B, 1B]
# A-elem in [-1B, 1B]


# So we need combination of all elems, whether they mean() = S
# Not combinatorics, they are continuous subsets
import random
from statistics import mean


def solution(A, S):
    i = 0
    S_mean_count = 0
    while i < len(A):
        j = i + 1
        while j <= len(A):
            if mean(A[i:j]) == S:
                S_mean_count += 1
                if S_mean_count > 1000000000:
                    return 1000000000
            j += 1
        i += 1

    return S_mean_count


if __name__ == '__main__':
    print(solution([2,1,3], 2))
    print(solution([0,4,3,-1], 2))
    print(solution([2,1,4], 3))
    print(solution([2], 2))

    g1000 = [4] * 25001 + random.sample(range(100000), 24999)
    random.shuffle(g1000)
    print(solution(g1000, 100))
