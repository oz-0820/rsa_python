import sympy
import numpy
import random
import math
import utils


# ASCIIコードの0x20から0x7Eの合計95文字を利用

def main():
    print('動作モードを選択してください。\n(鍵生成:1, 暗号化:2, 複合化:3)')
    mode = input('mode: ')

    if mode == '1':
        n = input('使う素数の桁数: ')
        n, e, lcm = utils.make_public_key(n)
        print(F'n: {n}\ne: {e}\nlcm: {lcm}')

        #print(F'{n}桁の適当な素数は\n{prime1}\nと\n{prime2}')

    if mode == '2':
        print('n,eを入力してください')
        #n = int(input('n: '))
        #e = int(input('e: '))
        n = 6521150106818279
        e = 988179092918
        print(F'n: {n}\ne: {e}')
        plain_char_list = list(input(F'暗号化します。\nASCIIコードの0x20から0x7Eまでの入力に対応しています。(計95文字)\ntext: '))
        plain_int_list = utils.char_text_to_int_list(plain_char_list)
        plain_int_list.reverse()
        plain = 0
        for i in range(len(plain_int_list)):
            plain += (plain_int_list[i]*pow(95, i))

        print(F'P: {plain}')

        int_crypt = 1
#        e_bin_list = list(bin(e)[2:]) # eを2進数に変換した
        e_bin_list = list(bin(3251)[2:])  # eを2進数に変換した
        lists = utils.exponentiation(2398, e_bin_list, 89711)  # n:(mod n)
        print(lists)

        #lists = utils.exponentiation(plain, e_bin_list, n)  # n:(mod n)
        #print(lists)



        #exponentiation(a, c, n):  # pow(a, pow(2, c), mod(n))


        """
        int_crypt = utils.exponentiation(plain, 2, i, n)  # pow(a, pow(b, c), mod(n))
        print(F'p^2^{i} = {int_crypt}')
        #int_crypt = int_crypt * numpy.mod((plain, pow(2, i)), n)
        #int_crypt = numpy.mod(int_crypt, n)
        """


        """
        int_crypt = plain
        for i in range(2, e):
            int_crypt = pow(int_crypt, 2) % n
            #print(F'i: {i}, int_crypt: {int_crypt}')
        #int_crypt = pow(plain, e) % n
        """
        print(F'crypt: {int_crypt}')

        crypt_int_list = utils.base_to_n(int_crypt, 95)
        print(F'crypt_int_list: {crypt_int_list}')

        crypt = utils.int_list_to_char_text(crypt_int_list)
        print(F'out_char: {crypt}')

    if mode == '3':
        crypt = input('複合化します。\ntext: ')








if __name__ == "__main__":
    main()





"""

    #ASCII to 数字
    input('平文を入力: ')
    int(ord(c))


if mode == 2:
    C = []
    print('暗号化(n,e確定)')
    n = int(input('n= '))
    e = int(input('e= '))
    char = input('文字(数値変換済み)= ')
    for i in range(len(char)):
        C.append(int(char.split(" ")))
    C.reverse()
    P = 0
    for i in range(len(C)):
        P = P + C[i] * pow(26, i)

    print(F'P= {P}')

    C = pow(P, e) % n
    print(F'P= {P}, pow(P, e)= {pow(P, e)}')
    print(F'複合化した結果{C}')



p = int(input('素数1： '))
q = int(input('素数2： '))

n = p * q
lcm = int((p-1) * (q-1) / 2)

pq_max = max(p, q)
print(F'lcm={lcm},pq_max={pq_max} ')

e = input('pq_max < e < lcmを入力してください\n')
print(F'公開鍵はn={n},e={e}')


def char_to_int(c):
    return int(ord(c))-65
    
"""