import sympy
import numpy
import random
import math


def make_prime(n):  # 重複しないn桁の素数を二つ返す
    n = int(n)
    prime1 = sympy.randprime(pow(10, (n-1)), pow(10, n))
    prime2 = sympy.randprime(pow(10, (n-1)), pow(10, n))

    if prime1 == prime2:
        make_prime(n)

    print(F'prime1: {prime1}\nprime2: {prime2}')

    return prime1, prime2


def int_len(num):
    return len(str(num))


def make_public_key(n):  # return n, e
    prime1, prime2 = make_prime(n)
    n = prime1 * prime2
    lcm = sympy.lcm(prime1-1, prime2-1)
    e_len = (len(str(max(prime1, prime2))) + len(str(lcm))) // 2
    e = random.randint(pow(10, e_len-1), pow(10, e_len))
    a = 0
    while not a == 1:
        a = sympy.gcd(e, lcm)
        e += 1
        #print(F'e: {e}')

    return n, e, lcm


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


"""

char_text   'abcdefg'
int_text    '123456789'
char_list   ['a', 'b', 'c', 'd', 'r', 'f', 'g']
int_list    ['1', '2', '3', '4', '5', '6', '7']

"""