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
import sys

banner = """\
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
            break

    return answer


def main():
    print(banner)
    print("CRACKING KEYBASE BY BRUTE FORCE!!!")
    a = input('Are you ready? [Y/n]')
    if a.lower().startswith('n'):
        return
    # load list of commands to try
    # 0 status means success
    # otherwise error
    with open("session/commands.txt") as f:
        commands = list(map(str.strip, f.readlines()))

    answer = crack(commands[13300:])
    if answer:
        print("CRACKED! :]")
        print("This command had success:")
        print(answer)
        with open("session/paperkey.txt", 'w') as f:
            f.write(answer)
        print("Result saved in session/paperkey.txt")
    else:
        print("None guess have success. Cracking didn't work! :[")

    os._exit(0)


if __name__ == '__main__':
    main()
