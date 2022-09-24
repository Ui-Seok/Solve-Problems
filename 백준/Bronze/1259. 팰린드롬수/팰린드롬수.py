while True:
    string = list(input())

    if string == ['0']:
        break
    
    mid = len(string) // 2

    if len(string) % 2 == 1:
        left = string[:mid]
        right = string[mid+1:]
        if left == right[::-1]:
            print('yes')
        else:
            print('no')
    else:
        left = string[:mid]
        right = string[mid:]
        if left == right[::-1]:
            print('yes')
        else:
            print('no')