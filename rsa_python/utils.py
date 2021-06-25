import copy

import sympy
import random


def make_prime(k_len):
    tmp_num_s = random.randint(pow(2, k_len-1), pow(2, k_len))
    tmp_num = copy.copy(tmp_num_s)
    if tmp_num % 2 == 0:
        tmp_num += 1
    t = 0
    tmp_num_key = [0] * 10
    while not sympy.isprime(tmp_num):
        if tmp_num < pow(2, k_len-1) or tmp_num > pow(2, k_len):
            make_prime(k_len)

        if tmp_num - tmp_num_s <= 100:
            tmp_num_key = make_tmp_num_key(tmp_num, tmp_num_key)
            tmp_num += 2
        else:
            tmp_num = add_tmp_num(tmp_num, tmp_num_key)

        t += 1
        print(F't:{t}\ntmp: {tmp_num - tmp_num_s}\n\n')
    return tmp_num


def add_tmp_num(tmp_num, tmp_num_key):
    try:
        if (tmp_num - tmp_num_key[0]) % 3 == 0:
            make_raise()
        elif (tmp_num - tmp_num_key[1]) % 5 == 0:
            make_raise()
        elif (tmp_num - tmp_num_key[2]) % 7 == 0:
            make_raise()
        elif (tmp_num - tmp_num_key[3]) % 11 == 0:
            make_raise()
        else:
            return tmp_num
    except Exception:
        return add_tmp_num(tmp_num + 2, tmp_num_key)


def make_raise():
    raise Exception


def make_tmp_num_key(tmp_num, tmp_num_key):
    if tmp_num % 3 == 0:
        tmp_num_key[0] = copy.copy(tmp_num)
    elif tmp_num % 5 == 0:
        tmp_num_key[1] = copy.copy(tmp_num)
    elif tmp_num % 7 == 0:
        tmp_num_key[2] = copy.copy(tmp_num)
    elif tmp_num % 11 == 0:
        tmp_num_key[3] = copy.copy(tmp_num)
    return tmp_num_key


def make_keys(key_len, e):  # return n, e, lcm, d
    p1_len = (key_len // 2) + 1
    p2_len = key_len - p1_len
    prime1 = sympy.randprime(pow(2, p1_len-1), pow(2, p1_len)-1)
    prime2 = sympy.randprime(pow(2, p2_len-1), pow(2, p2_len)-1)

    if prime1 == prime2:
        while prime1 == prime2:
            prime2 = sympy.randprime(pow(2, p2_len - 1), pow(2, p2_len) - 1)

    n = prime1 * prime2
    lcm = sympy.lcm(prime1-1, prime2-1)
    d, a, b = sympy.gcdex(e, lcm)
    d = int(d % lcm)

    return n, e, lcm, d


def e_input():
    e = input('eの値を選択する\na: 3，\nb: 5,\nc: 17,\nd: 257,\ne: 65537,(推奨)\nf: 131073,\ng: 262145,\n>> ')
    if e == 'a':
        return 3
    elif e == 'b':
        return 5
    elif e == 'c':
        return 17
    elif e == 'd':
        return 257
    elif e == 'e':
        return 65537
    elif e == 'f':
        return 131073
    elif e == 'g':
        return 262145
    else:
        print('入力エラー')
        return e_input()


def char_to_int(data):  # 文字列を突っ込むと数列を返す
    char_list = list(data)
    int_list = []
    for i in range(len(char_list)):
        int_list.append(ord(char_list[i])-32)
    int_list.reverse()
    int_data = 0
    for i in range(len(int_list)):
        int_data += int_list[i] * pow(95, i)
    return int_data


def int_to_char(data):  # 数列を突っ込むと文字列を返す
    i = 0
    while True:
        if data < pow(95, i+1):
            break
        i += 1

    int_list = []
    while i >= 0:
        int_text = 0
        a = pow(95, i)
        while int_text < 95:
            if (int_text + 1) * a > data:
                int_list.append(int_text)
                data -= int_text * a
                int_text += 95
            int_text += 1
        i -= 1

    char_list = []
    for i in range(len(int_list)):
        char_list.append(chr(int_list[i] + 32))
    char = ''.join(char_list)
    return char


def make_bin_expansion_list(data, bin_list, mod):  # 二進展開の一覧表を作る
    bin_expansion_list = [[0, data]]
    for i in range(1, len(bin_list)):
        data = i, pow(bin_expansion_list[i-1][1], 2) % mod
        bin_expansion_list.append(data)
    return bin_expansion_list


def multiply(bin_list, bin_expansion_list, mod):  # bin_listとbin_expansion_listから結果を計算する
    bin_list_re = list(reversed(bin_list))
    data = 1
    for i in range(len(bin_list_re)):
        if bin_list_re[i] == 1:
            data = data * bin_expansion_list[i][1] % mod
    return data


def bin_expansion(data, e, n):  # data ^ e (mod n)
    bin_list = list(map(int, list(bin(e)[2:])))
    bin_expansion_list = make_bin_expansion_list(data, bin_list, n)
    output = multiply(bin_list, bin_expansion_list, n)
    return output
