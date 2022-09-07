'''
시작 시간: 2시 25분
종료 시간: 3시 5분
'''

def solution(numbers, hand):
    result = []
    now_left_hand = [3, 0]
    now_right_hand = [3, 2]
    key_pad = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9],
               ['*', 0, '#']]
    L = [1, 4, 7, '*']
    R = [3, 6, 9, '#']
    mid = [2, 5, 8, 0]
    for num in numbers:
        x, y = find_xy(key_pad, num)
        if num in L:
            result.append('L')
            now_left_hand[0], now_left_hand[1] = x, y
        elif num in R:
            result.append('R')
            now_right_hand[0], now_right_hand[1] = x, y
        else:
            diff_l = abs(now_left_hand[0] - x) + abs(now_left_hand[1] - y)
            diff_r = abs(now_right_hand[0] - x) + abs(now_right_hand[1] - y)
            if diff_l > diff_r:
                result.append('R')
                now_right_hand[0], now_right_hand[1] = x, y
            elif diff_l < diff_r:
                result.append('L')
                now_left_hand[0], now_left_hand[1] = x, y
            else:
                if hand == 'left':
                    result.append('L')
                    now_left_hand[0], now_left_hand[1] = x, y
                elif hand == 'right':
                    result.append('R')
                    now_right_hand[0], now_right_hand[1] = x, y
    answer = "".join(result)
    return answer


def find_xy(key_pad, num):
    for i in range(4):
        for j in range(3):
            if key_pad[i][j] == num:
                x = i
                y = j
                return x, y