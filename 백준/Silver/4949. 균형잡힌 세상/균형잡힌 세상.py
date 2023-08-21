while True:
    check_line = input()
    branket = ["[", "]", "(", ")"]
    blank = [""]
    prev = ""

    if check_line == ".":
        break

    for st in check_line:
        if st in branket:
            if prev == "(" and st == ")":
                blank.pop()
                prev = blank[-1]
            elif prev == "[" and st == "]":
                blank.pop()
                prev = blank[-1]
            else:
                blank.append(st)
                prev = st
    blank.pop()
    if blank:
        print("no")
    else:
        print("yes")