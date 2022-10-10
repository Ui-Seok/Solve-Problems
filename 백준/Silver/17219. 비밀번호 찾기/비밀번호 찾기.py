n, m = map(int, input().split())
site = dict()
for _ in range(n):
    k, v = input().split()
    site[k] = v

for _ in range(m):
    get_site = input()
    print(site.get(get_site))