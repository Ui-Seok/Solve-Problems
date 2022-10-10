H, M = map(int, input().split())
if M-45 < 0:
  if H==0: H = 24
  H = H-1
  M = 15+M
  print(H, M)
else: print(H, M-45)