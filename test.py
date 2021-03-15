from typing import Dict, List, Tuple


def read_input_data(filename: str) -> List[str]:
    with open(filename, "r") as f:
        lines = [line[:-1] for line in f.readlines()]
    return lines


def format_input_data(lines: List[str]) -> Tuple[Dict[int, str], int]:
    # iとsのペアは"input.txt"に一行ずつ"i:s"形式で渡されます
    # mは"input.txt"の下から２番目の行で渡されます
    # "input.txt"の最終行は空行です
    splited_lines = [line.split(":") for line in lines[:-1]]
    pairs = {int(splited_line[0]): splited_line[1] for splited_line in splited_lines}
    return pairs, int(lines[-1])


def fizz_buzz_extended(pairs: Dict[int, str], m: int) -> None:
    # mがiの倍数ならsを出力
    answer_pairs = {i: s for i, s in pairs.items() if m % i == 0}

    # sはiの小さい順に出力してください(※iが小さい順に並んでいるとは限りません)
    sorted_pairs = sorted(answer_pairs.items(), key=lambda x: x[0])  # iでソート
    sorted_s_list = [pair[1] for pair in sorted_pairs]

    # どのsも出力されなければmを出力してください
    if len(sorted_s_list) == 0:
        print(m)
        return
    for s in sorted_s_list:
        print(s)


def main() -> None:
    # 入力は"input.txt"を読み込みます
    lines = read_input_data("./input.txt")
    pairs, m = format_input_data(lines)
    fizz_buzz_extended(pairs, m)


main()