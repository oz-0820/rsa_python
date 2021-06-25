import utils
# ASCIIコードの0x20から0x7Eの合計96文字を利用


def main():
    print('まず鍵を作ります')
    n, e, d = mode1()
    crypt = 0
    while True:
        try:
            print('\n動作モードを選択してください。\n(鍵生成:1, 暗号化:2, 複合化:3, 現在の値を確認:4, 終了:5)')
            mode = input('mode: ')
            if mode == '1':
                n, e, d = mode1()
            elif mode == '2':
                crypt = mode2(n, e)
            elif mode == '3':
                mode3(crypt, n, d)
            elif mode == '4':
                mode4(n, e, d, crypt)
            elif mode == '5':
                break
            else:
                raise ValueError
        except ValueError:
            print('入力値が不正です')


def mode1():
    key_len = int(input('4096bit以下を推奨。ただし、あまりにも小さいとエラーが出ます。\n鍵の長さ(bit): '))
    e = utils.e_input()

    n, e, lcm, d = utils.make_keys(key_len, e)
    print(F'n: {n}\ne: {e}\nd: {d}')
    return n, e, d


def mode2(n, e):
    print('n,eを入力してください.\n先ほど生成した鍵を利用する場合は"n: 0"と入力してください')
    n_ = input('n: ')
    if n_ != '0':
        n = int(n_)
        e = int(input('e: '))
    else:
        print(F'n: {n}\ne: {e}')

    char_plain = input(F'暗号化します。\nASCIIコードの0x20から0x7Eまでの入力に対応しています。(計96文字)\nつまりは半角英数と記号\ntext: ')
    int_plain = utils.char_to_int(char_plain)

    int_crypt = utils.bin_expansion(int_plain, e, n)
    # 実はpowにmodと二進展開の機能があるとか知りたくなかった
    # utils.bin_expansion() == pow()
    # int_crypt = pow(int_plain, e, n)

    char_crypt = utils.int_to_char(int_crypt)
    print(F'crypt: {char_crypt}')
    return char_crypt


def mode3(crypt, n, d):
    char_crypt = input('複合化します。\n先ほど生成した鍵・暗号を利用する場合は"text: 0"と入力してください\ntext: ')
    if char_crypt == '0':
        char_crypt = crypt
        print(F'crypt: {char_crypt}\nn: {n}\nd: {d}')
    else:
        n = int(input('n: '))
        d = int(input('d: '))

    crypt = utils.char_to_int(char_crypt)
    int_plain = utils.bin_expansion(crypt, d, n)
    # 実はpowにmodと二進展開の機能があるとか知りたくなかった
    # utils.bin_expansion() == pow()
    # int_plain = pow(crypt, d, n)
    char_plain = utils.int_to_char(int_plain)
    print(F'plain: {char_plain}')


def mode4(n, e, d, crypt):
    print(F'n: {n}\ne: {e}\nd: {d}\ncrypt: {crypt}\n')


if __name__ == "__main__":
    main()

