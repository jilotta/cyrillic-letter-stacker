Cyrillic letter stacker
=======================
Stacks one phrase in Cyrillic script on top of another using Unicode characters from "Cyrillic Extended-A", "Cyrillic Extended-B", "Combining Diacritical Marks", "Combining Diacritical Marks Supplement".

Not all letters are in these blocks. For example, letters "э", "ё" and "я" raise a `KeyError`, "й" is substituted by "ü", and a lot of other letters are subtituted by their Latin look-alikes because of compatibility issues.

A lot of fonts do not support the characters, and some fonts support half. For example, Open Sans shows tofus.

Surprisingly, Iosevka, a programming font, supports all of the characters used.
