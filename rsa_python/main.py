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
        key_len = int(input('鍵の長さ(bit): '))
        e = utils.e_input()
        # n = input('使う素数の桁数: ')
        n, e, lcm, d = utils.make_keys(key_len, e)
        print(F'n: {n}\ne: {e}\nlcm: {lcm}\nd: {d}')
        """
        file = open('keys.txt', 'w')
        for i in range(50):
            n, e, lcm, d = utils.make_keys(512, 65537)
            data = [n, e, lcm, d]
            print(F'n: {n}\ne: {e}\nlcm: {lcm}\nd: {d}')

            file.write(str(data) + "\n")
        file.close()
        """

    if mode == '2':
        print('n,eを入力してください')
        n = int(input('n: '))
        e = int(input('e: '))
        plain = int(input('p: '))
        # n = 89711
        # e = 65537
        # plain = 2398
        # print(F'n: {n}\ne: {e}\np: {plain}')

        # plain_char_list = list(input(F'暗号化します。\nASCIIコードの0x20から0x7Eまでの入力に対応しています。(計95文字)\ntext: '))
        # plain_int_list = utils.char_text_list_to_int_text_list(plain_char_list)
        # print(utils.int_text_list_to_int(plain_int_list, 26))

        crypt = utils.bin_expansion(plain, e, n)  # plain ^ e (mod n)

        print(F'crypt: {crypt}')

    if mode == '3':
        # crypt = input('複合化します。\ntext: ')
        crypt = int(input('crypt: '))
        n = int(input('n: '))
        d = int(input('d: '))

        plain = utils.bin_expansion(crypt, d, n)

        print(F'plain: {plain}')


if __name__ == "__main__":
    main()

