qwerty = '`1234567890-=QWERTYUIOP[]\ASDFGHJKL;\'ZXCVBNM,./'

while True:
    try:
        string = input()
        new_string = ''

        for i in string:
            if i in qwerty:
                idx = qwerty.index(i)
                new_string += qwerty[idx - 1]
            else:
                new_string += i
                
        print(new_string)
    except:
        break