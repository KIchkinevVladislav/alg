N, M = map(int, input().split())
sequence = list(map(int, input().split()))

def find_element(L, R):
    min_val = min(sequence[L:R+1])
    for i in range(L, R+1):
        if sequence[i] != min_val:
            return sequence[i]
    return "NOT FOUND"

for _ in range(M):
    L, R = map(int, input().split())
    result = find_element(L, R)
    print(result)