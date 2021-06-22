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

        n, e, lcm, d = utils.make_keys(key_len, e)
        print(F'n: {n}\ne: {e}\nlcm: {lcm}\nd: {d}')

    if mode == '2':
        print('n,eを入力してください')
        n = int(input('n: '))
        e = int(input('e: '))
        # plain = int(input('p: '))

        plain_char = input(F'暗号化します。\nASCIIコードの0x20から0x7Eまでの入力に対応しています。(計95文字)\nつまりは半角英数と記号\ntext: ')
        plain = utils.char_to_int(plain_char, 95)

        print(F'plain_int: {plain}')

        crypt = utils.bin_expansion(plain, e, n)  # plain ^ e (mod n)

        print(F'crypt: {crypt}')

    if mode == '3':
        crypt_char_list = list(input('複合化します。\ntext: '))
        crypt_int_list = utils.char_text_list_to_int_text_list(crypt_char_list)
        crypt = utils.int_text_list_to_int(crypt_int_list, 95)
        # crypt = input('複合化します。\ntext: ')
        #  crypt = int(input('crypt: '))
        n = int(input('n: '))
        d = int(input('d: '))

        plain = utils.bin_expansion(crypt, d, n)

        print(F'plain: {plain}')


if __name__ == "__main__":
    main()

