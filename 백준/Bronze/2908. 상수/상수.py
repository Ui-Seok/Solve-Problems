num_A, num_B = map(str, input().split())
num_A = int(num_A[::-1])
num_B = int(num_B[::-1])

if num_A > num_B: print(num_A)
else: print(num_B)