def is_prefix(a, b):
    return b.startswith(a)

def dfs(i, strings, memo):
    if memo[i] != -1:
        return memo[i]

    max_len = 1
    for j in range(len(strings)):
        if i != j and is_prefix(strings[i], strings[j]):
            max_len = max(max_len, 1 + dfs(j, strings, memo))

    memo[i] = max_len
    return max_len

while True:
    N = int(input())
    if N == 0:
        break

    strings = [input().strip() for _ in range(N)]
    strings.sort()

    memo = [-1] * N
    resposta = 0
    for i in range(N):
        resposta = max(resposta, dfs(i, strings, memo))

    print(resposta)
