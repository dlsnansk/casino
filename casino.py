#!/usr/bin/env python3
# casino.py
# A simple gambling game for relaxation and passing the time

import keyboard as k
import random as r
import time as t
import sys, os

nv = '\033[?25l'
v = '\033[?25h'

smb = ('6', '7', '9', '?', '$')
slot = ['X', 'X', 'X']

hello = '''
===== W E L C O M E =====
========== T O ==========
========= T H E =========

=========================
====== C A S I N O ======
=========================

  [  ENTER -> START  ]
  [  ESC   -> QUIT   ]
'''

bye = '''
GOODBYE! HAVE A NICE DAY!  :)
'''

def cl():
    os.system('cls'if os.name=='nt'else'clear')

def slots(slot):
    print('  |   |   |   |')
    print(f'--|-{slot[0]}-|-{slot[1]}-|-{slot[2]}-|--')
    print('  |   |   |   |')

def spin():
    global slot
    cl()
    print(f'{nv}{hello}')
    while True:
        while True:
            if k.is_pressed('enter'):
                break
            if k.is_pressed('esc'):
                print(f'{v}{bye}')
                sys.exit()
            t.sleep(0.05)

        for i in range(15):
            cl()
            print('SPINNING...\n')
            slot = [r.choice(smb), r.choice(smb), r.choice(smb)]
            slots(slot)
            t.sleep(0.15)

        cl()
        print('RESULTS\n')
        slots(slot)

        print()
        if slot[0] == slot[1] == slot[2]:
            print('[!!!] EXCELLENT! ALL THREE IN A ROW! [!!!]')
        elif slot[0] == slot[1] or slot[1] == slot[2]:
            print('[!] Not bad. Two identical ones. [!]')
        else:
            print('[X_X] no identical ones [X_X]')
        print()

        print('''
[  ENTER -> START  ]
[  ESC   -> QUIT   ]
''')

        while True:
            if k.is_pressed('enter'):
                break
            if k.is_pressed('esc'):
                print(f'{v}{bye}')
                sys.exit()
            t.sleep(0.05)

try:
    spin()
except KeyboardInterrupt:
    print(f'{v}{bye}')
    sys.exit()
except Exception as e:
    print(f'[ERROR] -> {e}')
    sys.exit()
