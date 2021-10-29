from . import alphabet


def rewrite(input_string: str):
    return " ".join([alphabet.alphabet.get(c,c) for c in input_string.replace(" ","")])
