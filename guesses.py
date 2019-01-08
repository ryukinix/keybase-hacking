#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#    Copyright © 2019 Manoel Vilela
#
#    @project: Keybase Hacking!
#     @author: Manoel Vilela
#      @email: manoel_vilela@engineer.com
#

"""
Generate the paperkey guesses for cracking!
"""


import io
from typing import List


def parse(f: io.TextIOWrapper) -> List[str]:
    "Parse a file with read permissions as list of words"
    return list(map(str.strip, f.readlines()))


def to_text(paperkey: List[str]) -> str:
    "Join the paperkey words as a string"
    return ' '.join(paperkey)


def generate_guesses(word: str, paperkey: List[str]):
    "Generate unique guesses based on a word for each placement."
    if word in paperkey:
        return []
    guesses = []
    for k in range(2, len(paperkey)):
        g = paperkey.copy()
        g.insert(k, word)
        guesses.append(g)
    return guesses


def main():
    # load english words
    with open('data/english_dic.txt') as f:
        dic = parse(f)

    # load incomplete paperkey
    with open('data/paperkey_incomplete.txt') as f:
        paperkey = parse(f)

    # generate and print guesses
    for word in dic:
        for guess in generate_guesses(word, paperkey):
            print(to_text(guess))


if __name__ == '__main__':
    main()
