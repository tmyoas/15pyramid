# ans format: 5 * 5 array
# [[a01, a02, a03, a04, a05],
#  [a06, a07, a08, a09, -1 ],
#  [a10, a11, a12, -1,  -1 ],
#  [a13, a14, -1 , -1,  -1 ],
#  [a15, -1 , -1 , -1,  -1 ]]
# Then, ans[x][y] (1 < x < 4, 0 < y < 4, x + y =< 4) = abs(ans[x - 1][y] - ans[x][y + 1])
# -1 is no-use-flag.

# 15 is always used in ans[0][n]
# max(a[0][n], a[0][n + 1]) > a[1][n] because abs(a[0][n] - a[0][n + 1]) = a[1][n]
# So, 1 =< a[1][n] < 14.

# a[1][n] is fixed by only a[0][n] and a[0][n + 1].
# So, we can exclude a[1][n] from a[0].

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
    for i in range(1, len(arr_calc)):
        for j in range(len(arr_calc[0]) - 1):
            if (arr_calc[i - 1][j] == -1) or (arr_calc[i - 1][j + 1] == -1):
                arr_calc[i][j] = -1
            else:
                arr_calc[i][j] = abs(arr_calc[i - 1][j] - arr_calc[i - 1][j + 1])

    return arr_calc


def check_correct(arr_calc):

    check_arr = [0 for i in range(16)]
    check_arr[0] = -1
    for i in arr_calc:
        for j in i:
            if j != -1:
                check_arr[j] += 1

    return 0 not in check_arr


def check_calc(arr_calc):
    check_arr = [0 for i in range(16)]
    check_arr[0] = -1
    for i in arr_calc:
        for j in i:
            if j != -1:
                check_arr[j] += 1

    # {1, 0, -1} or {1, -1} is only accepted.
    return len(set(check_arr)) == 2 or len(set(check_arr)) == 3


def check_skip(arr, pos, ans_tmp):
    arr.insert(pos, 15)
    ans_tmp[0] = arr
    ans_tmp = calc_all(ans_tmp)

    return check_calc(ans_tmp)


if __name__ == '__main__':
    start = time.time()
    ans = init()

    with open('log_3.txt', mode='w') as f:

        for m in range(0, 3):
            for i in range(1, 8):
                for j in range(1, 15):
                    ans_n_0 = [i, j, -1, -1]
                    if j == i:
                        continue
                    else:
                        if not check_skip(ans_n_0, m, ans):
                            f.write(','.join([str(n) for n in ans_n_0]) + '\n')
                            continue
                    for k in range(1, 15):
                        ans_n_0 = [i, j, k, -1]
                        if len(ans_n_0) != len(set(ans_n_0)):
                            continue
                        else:
                            if not check_skip(ans_n_0, m, ans):
                                f.write(','.join([str(n) for n in ans_n_0]) + '\n')
                                continue
                        for l in range(1, 15):
                            ans_n_0 = [i, j, k, l]
                            if len(ans_n_0) != len(set(ans_n_0)):
                                continue
                            else:
                                # check_skip is no useful for decreasing steps because
                                # ans_n_0 is already fixed in this line,
                                # so loop-count is no change using it or not.
                                ans_n_0.insert(m, 15)
                                f.write(','.join([str(n) for n in ans_n_0]) + '\n')
                                ans[0] = ans_n_0
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

    print('Processing speed: ' + str(time.time() - start) + ' s')