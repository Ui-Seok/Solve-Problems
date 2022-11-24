n, k = map(int, input().split())

pac_n = 1
for i in range(1, n+1):
    pac_n *= i

pac_k = 1
for j in range(1, k+1):
    pac_k *= j

pac_n_k = 1
for k in range(1, n-k+1):
    pac_n_k *= k

print(pac_n // (pac_k * pac_n_k))