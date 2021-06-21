import sympy
import numpy
import random
import math


def make_public_key():  # return n, e, lcm, d
    key_len = int(input('鍵の長さ(bit): '))
    # e = input('eの値を選択する\na: 3，\nb: 5,\nc: 17,\nd: 257,\ne: 65537,(推奨)\nf: 131073,\ng: 262145,\n>> ')
    e = e_input()

    p1_len = (key_len // 2) + 1
    p2_len = key_len - p1_len
    prime1 = sympy.randprime(pow(2, p1_len-1), pow(2, p1_len)-1)
    prime2 = sympy.randprime(pow(2, p2_len-1), pow(2, p2_len)-1)
    n = prime1 * prime2
    lcm = sympy.lcm(prime1-1, prime2-1)
    d, a, b = sympy.gcdex(e, lcm)

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


def char_text_to_int_list(char_list):
    int_list = []
    for i in range(len(char_list)):
        int_list.append(ord(char_list[i])-31)
    print(F'int_list: {int_list}')
    return int_list


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



def int_to_char(data, word_count):
    # cryptogram =
    i = 0
    while pow(word_count, i) < data:
        i += 1


char_text   'abcdefg'
int_text    '123456789'
char_list   ['a', 'b', 'c', 'd', 'r', 'f', 'g']
int_list    ['1', '2', '3', '4', '5', '6', '7']

"""