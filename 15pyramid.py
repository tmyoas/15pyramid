# ans format: 5 * 5 array
# [[a01, a02, a03, a04, a05],
#  [a06, a07, a08, a09, -1 ],
#  [a10, a11, a12, -1,  -1 ],
#  [a13, a14, -1 , -1,  -1 ],
#  [a15, -1 , -1 , -1,  -1 ]]
# Then, ans[x][y] (1 < x < 4, 0 < y < 4, x + y =< 4) = abs(ans[x - 1][y] - ans[x][y + 1])

# Brute force

import time

# Global init
USE_NUM = range(1, 16)


def init():
    arr_calc = [[0 for i in range(5)] for j in range(5)]
    for i, list_i in enumerate(arr_calc):
        for j, num in enumerate(list_i):
            if (i + j) > 4:
                arr_calc[i][j] = -1

    return arr_calc


def set_num(arr_calc, x, y, num):
    arr_calc[x][y] = num

    return arr_calc


def calc_next(arr_calc, x, y):
    arr_calc[x][y] = abs(arr_calc[x - 1][y] - arr_calc[x - 1][y + 1])

    return arr_calc


def calc_all(arr_calc):
    for i in range(len(arr_calc)):
        for j in range(len(arr_calc[0])):
            if (i > 0) and (arr_calc[i][j] != -1):
                arr_calc[i][j] = abs(arr_calc[i - 1][j] - arr_calc[i - 1][j + 1])

    return arr_calc


def check_correct(arr_calc):
    # flag = False
    check_arr = [0 for i in range(16)]
    check_arr[0] = -1
    for i in arr_calc:
        for j in i:
            if j != -1:
                check_arr[j] += 1

    return 0 not in check_arr


if __name__ == '__main__':
    start = time.time()
    ans = init()

    with open('log.txt', mode='w') as f:

        for i in range(1, 16):
            for j in range(1, 16):
                for k in range(1, 16):
                    for l in range(1, 16):
                        for m in range(1, 16):
                            tmp = [i, j, k, l, m]
                            if len(tmp) == len(set(tmp)):
                                f.write(','.join([str(n) for n in tmp]) + '\n')
                                for n, num in enumerate(tmp):
                                    ans[0][n] = num
                                ans = calc_all(ans)
                                if check_correct(ans):
                                    print(ans)
                                    break
                                else:
                                    continue
                                break
                        else:
                            continue
                        break
                    else:
                        continue
                    break
                else:
                    continue
                break
            else:
                continue
            break

    print('Processing speed: ' + str(time.time() - start) + ' s')