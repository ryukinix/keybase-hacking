#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#    Copyright © 2019 Manoel Vilela
#
#    @project: Keybase Hacking!
#     @author: Manoel Vilela
#      @email: manoel_vilela@engineer.com
#


from tqdm import tqdm
import os

banner="""\
██ ▄█▀▓█████▓██   ██▓ ▄▄▄▄    ▄▄▄        ██████ ▓█████
 ██▄█▒ ▓█   ▀ ▒██  ██▒▓█████▄ ▒████▄    ▒██    ▒ ▓█   ▀
▓███▄░ ▒███    ▒██ ██░▒██▒ ▄██▒██  ▀█▄  ░ ▓██▄   ▒███
▓██ █▄ ▒▓█  ▄  ░ ▐██▓░▒██░█▀  ░██▄▄▄▄██   ▒   ██▒▒▓█  ▄
▒██▒ █▄░▒████▒ ░ ██▒▓░░▓█  ▀█▓ ▓█   ▓██▒▒██████▒▒░▒████▒
▒ ▒▒ ▓▒░░ ▒░ ░  ██▒▒▒ ░▒▓███▀▒ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░░░ ▒░ ░
░ ░▒ ▒░ ░ ░  ░▓██ ░▒░ ▒░▒   ░   ▒   ▒▒ ░░ ░▒  ░ ░ ░ ░  ░
░ ░░ ░    ░   ▒ ▒ ░░   ░    ░   ░   ▒   ░  ░  ░     ░
░  ░      ░  ░░ ░      ░            ░  ░      ░     ░  ░
              ░ ░           ░
 ██░ ██  ▄▄▄       ▄████▄   ██ ▄█▀ ██▓ ███▄    █   ▄████
▓██░ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ ▓██▒ ██ ▀█   █  ██▒ ▀█▒
▒██▀▀██░▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▒██▒▓██  ▀█ ██▒▒██░▄▄▄░
░▓█ ░██ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ░██░▓██▒  ▐▌██▒░▓█  ██▓
░▓█▒░██▓ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄░██░▒██░   ▓██░░▒▓███▀▒
 ▒ ░░▒░▒ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒░▓  ░ ▒░   ▒ ▒  ░▒   ▒
 ▒ ░▒░ ░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░ ▒ ░░ ░░   ░ ▒░  ░   ░
 ░  ░░ ░  ░   ▒   ░        ░ ░░ ░  ▒ ░   ░   ░ ░ ░ ░   ░
 ░  ░  ░      ░  ░░ ░      ░  ░    ░           ░       ░
                  ░
"""


def crack(commands):
    answer = None
    for command in tqdm(commands):
        print('> ' + command)
        status = os.system(command)
        if status == 0:
            answer = command

    return answer


def main():
    print(banner)
    # load list of commands to try
    # 0 status means success
    # otherwise error
    with open("session/commands.txt") as f:
        commands = list(map(str.strip, f.readlines()))

    print("CRACKING KEYBASE BY BRUTE FORCE!!!")
    answer = crack(commands)
    if answer:
        print("CRACKED! :]")
        print("This command had success:")
        print(answer)
        with open("session/result.txt", 'w') as f:
            f.write(answer)
    else:
        print("None guess have success. Cracking didn't work! :[")


if __name__ == '__main__':
    main()
