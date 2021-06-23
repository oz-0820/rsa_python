import sympy
import numpy
import random
import math


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
    d = d % lcm

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


def char_to_int(data, m):  # 文字列と文字の種類数を突っ込むと一つの数として返す
    char_list = list(data)
    int_list = []
    for i in range(len(char_list)):
        int_list.append(ord(char_list[i])-31)
    # int_list = char_text_list_to_int_text_list(char_list)
    return int_text_list_to_int(int_list, m)


def char_text_list_to_int_text_list(char_list):  # charなリストを突っ込むとintなリストに変換して返してくれる
    int_list = []
    for i in range(len(char_list)):
        int_list.append(ord(char_list[i])-31)
    return int_list


def int_text_list_to_int(data, count):  # int_listなデータと文字数を突っ込むと一つの数になって帰ってくる
    data.reverse()
    int_data = 0
    for i in range(len(data)):
        int_data += data[i] * pow(count, i)
    return int_data


# def int_to_char(data, m):




def int_list_to_char_text(int_list):
    char_text = ''
    for i in range(len(int_list)):
        #print(int_list[i])
        #print(F'type: {type(int_list[i])}')
        char_text += chr(int_list[i] + 31)
    return char_text


def base_to_n(x, n):  # x, n : 変換元, n進数へ
    int_list = []
    count = 0
    while pow(n, count) <= x:
        count += 1
    count -= 1
    for a in range(0, count+1):
        h = 0
        while h*pow(n, count) <= x:
            h += 1
        h -= 1
        x -= h*pow(n, count)
        int_list.append(h)
        count -= 1

    return int_list


def exponentiation(a, c, n):  # pow(a, pow(2, c), mod(n))
    output = a
    for i in range(1, pow(2, c)):
        #print(F'count{i}')
        output = output * a
        output = numpy.mod(output, n)
    return output


def p_2_n_mod_m(p, n, m):
    print(F'p: {p}, n: {n}, m: {m})')
    output = p
    for i in range(1, n):
        print(F'Count: {i}')
        output = numpy.mod(output * p * pow(2, n-1), m)
        #output = numpy.mod(output, m)

    return output


def exponentiation(plain, e_bin_list, n):  # n:(mod n)
    expon = []
    e_bin_list.reverse()
    for i in range(0, len(e_bin_list)):
        if e_bin_list[i] == '1':
            a = p_2_n_mod_m(plain, i, n)
            expon.append(a)
            print(F'p^2^{i} = {a}')
    return expon


def dec_to_bin_list(dec, mod, plain):
    bin_list = list(map(int, list(bin(dec)[2:])))
    # [1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1]
    bin_list.reverse()
    # [[0, 2398], [1, 8900]]
    # return_list = []
    # ['1', '1', '0', '0', '1', '0', '1', '1', '0', '0', '1', '1']

    for i in range(len(bin_list)):
        if bin_list[i] == 1:
            print(F'P^2^{i} = {pow(plain, pow(2, i))%89711}')


def encrypt(plain, e, mod):
    e_bin_list = list(map(int, list(bin(e)[2:])))
    e_bin_list.reverse()
    cryptogram = 1
    for i in range(len(e_bin_list)):
        if e_bin_list[i] == 1:
            data = pow(plain, pow(2, i)) % mod
            print(F'P^2^{i} = {data}')
            cryptogram *= data
            cryptogram = cryptogram % mod
            print(F'cryptogram:{cryptogram}')

            # [[i, data], [i, data]]


def make_bin_expansion_list(data, bin_list, mod):  # 二進展開の一覧表を作る
    bin_expansion_list = [[0, data]]
    for i in range(1, len(bin_list)):
        data = i, pow(bin_expansion_list[i-1][1], 2) % mod
        bin_expansion_list.append(data)
    return bin_expansion_list


def make_bin_list(data):  # 十進をintな二進にして一桁ずつlistに格納
    bin_list = list(map(int, list(bin(data)[2:])))
    return bin_list


def multiply(bin_list, bin_expansion_list, mod):  # bin_listとbin_expansion_listから最後の研鑽する
    bin_list_re = list(reversed(bin_list))
    data = 1
    for i in range(len(bin_list_re)):
        if bin_list_re[i] == 1:
            # print(i)
            data = data * bin_expansion_list[i][1] % mod
    return data


def bin_expansion(data, e, n):  # plain ^ e (mod n)
    # 入力： p^e (mod n), plain, e, n
    # 出力:
    e_bin_list = list(map(int, list(bin(e)[2:])))
    bin_expansion_list = make_bin_expansion_list(data, e_bin_list, n)
    output = multiply(e_bin_list, bin_expansion_list, n)
    return output


def int_to_char_list(data, n):
    # cryptogram =
    count = 0
    while pow(n, count) < data:
        count += 1
    count -= 1

    for i in count:
        a = 1
        # while a < data:

    return i

