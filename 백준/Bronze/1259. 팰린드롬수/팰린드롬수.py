while True:
    a = list(input())
    if a == ['0']:
        break
    
    if len(a) % 2:
        if a[:len(a)//2] == a[:len(a)//2:-1]:
            print('yes')
        else:
            print('no')

    else:
        if a[:len(a)//2] == a[:len(a)//2 - 1:-1]:
            print('yes')
        else:
            print('no')