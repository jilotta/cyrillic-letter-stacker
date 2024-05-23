stack_cyr = {
    "а": "\u0363",
    "б": "\u2de0",
    "в": "\u2de1",
    "г": "\u2de2",
    "д": "\u2de3",
    "е": "\u0364",
    # ё
    "ж": "\u2de4",
    "з": "\u2de5",
    "и": "\uA675",  # "\u0367" -- u
    "й": "\u1df4",  # u with dieresis
    "к": "\u2de6",
    "л": "\u2de7",
    "м": "\u2de8",
    "н": "\u2de9",
    "о": "\u0366",
    "п": "\u2deb",
    "р": "\u1dee",
    "с": "\u0368",
    "т": "\u2dee",
    "у": "\uA677",
    "ф": "\uA69E",
    "х": "\u036f",
    "ц": "\u2df0",
    "ч": "\u2df1",
    "ш": "\u2df2",
    "щ": "\u2df3",
    "ъ": "\uA678",
    "ы": "\uA679",
    "ь": "\uA67A",
    # э
    "ю": "\u2dfb",
    # я
    " ": "",
}


def stack(top: str, bottom: str):
    from itertools import zip_longest

    result = ""
    for t in zip_longest(top, btm, fillvalue=" "):
        result += t[1] + stack_cyr[t[0]]
    return result


if __name__ == "__main__":
    top = input(
        "Верхний текст (только кириллица нижнего регистра). Не поддерживаются Э, Я, Ё: "
    ).lower()
    btm = input("Нижний текст: ")

    print(stack(top, btm))
