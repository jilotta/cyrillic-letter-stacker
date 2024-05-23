latin_stack = {
    "a": "\u0363",
    "b": "\u1DE8",
    "c": "\u0368",
    "d": "\u0369",
    "e": "\u0364",
    "f": "\u1DEB",
    "g": "\u1DDA",
    "h": "\u036A",
    "i": "\u0365",
    "k": "\u1DDC",
    "l": "\u1DDD",
    "m": "\u036B",
    "n": "\u1DE0",
    "o": "\u0366",
    "p": "\u1DEE",
    "r": "\u036C",
    "s": "\u1DE4",
    "t": "\u036d",
    "u": "\u0367",
    "v": "\u036e",
    "w": "\u1DF1",
    "x": "\u036f",
    "y": "\uA677",  # actually a cyrillic У
    "z": "\u1DE6",
}

cyrillic_stack = {
    "а": latin_stack["a"],
    "б": "\u2de0",
    "в": "\u2de1",
    "г": "\u2de2",
    "д": "\u2de3",
    "е": latin_stack["e"],
    # ё
    "ж": "\u2de4",
    "з": "\u2de5",
    "и": "\uA675",  # "\u0367" -- latin u, more compatible
    "й": "\u1df4",  # u with dieresis
    "к": "\u2de6",
    "л": "\u2de7",
    "м": "\u2de8",
    "н": "\u2de9",
    "о": latin_stack["o"],
    "п": "\u2deb",
    "р": latin_stack["p"],
    "с": latin_stack["c"],
    "т": "\u2dee",
    "у": latin_stack["y"],
    "ф": "\uA69E",
    "х": latin_stack["x"],
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
}

whole_stack = cyrillic_stack | latin_stack


def stack(top: str, bottom: str):
    from itertools import zip_longest

    result = ""
    for t in zip_longest(top, bottom, fillvalue=" "):
        result += t[1] + whole_stack[t[0]]
    return result


if __name__ == "__main__":
    top = input(
        "Top text. Lowercase Russian Cyrillic or Base Latin except Э, Ё, Я, J, Q: "
    ).lower()
    bottom = input("Bottom text: ")

    print(stack(top, bottom))
