latin_stack = {
    "a": "\u0363",
    "b": "\u1dE8",
    "c": "\u0368",
    "d": "\u0369",
    "e": "\u0364",
    "f": "\u1deb",
    "g": "\u1dda",
    "h": "\u036a",
    "i": "\u0365",
    "k": "\u1ddc",
    "l": "\u1ddd",
    "m": "\u036b",
    "n": "\u1De0",
    "o": "\u0366",
    "p": "\u1dee",
    "r": "\u036c",
    "s": "\u1de4",
    "t": "\u036d",
    "u": "\u0367",
    "v": "\u036e",
    "w": "\u1df1",
    "x": "\u036f",
    "y": "\ua677",  # actually a cyrillic У
    "z": "\u1de6",
}

cyrillic_stack = {
    "а": "\u2df6",
    "б": "\u2de0",
    "в": "\u2de1",
    "г": "\u2de2",
    "д": "\u2de3",
    "е": "\u2dF7",
    # ё
    "ж": "\u2de4",
    "з": "\u2de5",
    "и": "\ua675",
    "й": "\u1df4",  # actually a latin u with dieresis
    "к": "\u2de6",
    "л": "\u2de7",
    "м": "\u2de8",
    "н": "\u2de9",
    "о": "\u2dea",
    "п": "\u2deb",
    "р": "\u2dec",
    "с": "\u2ded",
    "т": "\u2dee",
    "у": "\ua677",
    "ф": "\ua69e",
    "х": "\u2def",
    "ц": "\u2df0",
    "ч": "\u2df1",
    "ш": "\u2df2",
    "щ": "\u2df3",
    "ъ": "\ua678",
    "ы": "\ua679",
    "ь": "\ua67a",
    # э
    "ю": "\u2dfb",
    # я
}

whole_stack = cyrillic_stack | latin_stack | {" ": ""}


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
