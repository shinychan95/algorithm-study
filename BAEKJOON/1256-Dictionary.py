from math import factorial as f


def comb(n, m):
    return f(n + m) // f(n) // f(m)


def shift(n, m, k):
    if k <= m + 1:
        return "a" * (n - 1) + "z" * (k - 1) + "a" + "z" * (m - k + 1)

    c = comb(n - 1, m)
    if k <= c:
        return "a" + shift(n - 1, m, k)
    else:
        return "z" + shift(n, m - 1, k - c)


N, M, K = map(int, input().split())

if comb(N, M) < K:
    print("-1")

else:
    print("".join(shift(N, M, K)))
