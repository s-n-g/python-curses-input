#!/bin/python
######################################################################
# test.py
import curses
import curses.ascii
from sys import version_info

import locale
locale.setlocale(locale.LC_ALL, '')


def get_char(win):
    def get_check_next_byte():
        char = win.getch()
        if 128 <= char <= 191:
            return char
        else:
            raise UnicodeError

    bytes = []
    char = win.getch()



    if char in (curses.KEY_ENTER, ord('\n'), ord('\r')):
        win.addstr('[ENTER]\n')
    elif char in (curses.KEY_EXIT, 27):
        win.addstr('[ESCAPE]')
        return '[ESCAPE]'
    elif char in (curses.KEY_RIGHT, curses.ascii.ACK):
        win.addstr('[KEY_RIGHT]')
    elif char in (curses.KEY_LEFT, ):
        win.addstr('[KEY_LEFT]')
    elif char in (curses.KEY_HOME, curses.ascii.SOH):
        win.addstr('[KEY_HOME]')
    elif char in (curses.KEY_END, curses.ascii.ENQ):
        win.addstr('[KEY_END]')
    elif char in (curses.KEY_DC, curses.ascii.EOT):
        win.addstr('[KEY_DELETE]')
    elif char in (curses.KEY_BACKSPACE, curses.ascii.BS , 127):
        win.addstr('[KEY_BACKSPACE]')
    elif char in (curses.KEY_UP, curses.ascii.DLE):
        win.addstr('[KEY_UP]')
    elif char in (curses.KEY_DOWN, curses.ascii.SO):
        win.addstr('[KEY_DOWN]')
    elif char in (curses.ascii.VT, ):
        win.addstr('[DEL_TO_LINE_END]')
    elif char <= 127:
        # 1 bytes
        bytes.append(char)
    #elif 194 <= char <= 223:
    elif 192 <= char <= 223:
        # 2 bytes
        bytes.append(char)
        bytes.append(get_check_next_byte())
    elif 224 <= char <= 239:
        # 3 bytes
        bytes.append(char)
        bytes.append(get_check_next_byte())
        bytes.append(get_check_next_byte())
    elif 240 <= char <= 244:
        # 4 bytes
        bytes.append(char)
        bytes.append(get_check_next_byte())
        bytes.append(get_check_next_byte())
        bytes.append(get_check_next_byte())
    #print('bytes = {}'.format(bytes))
    if version_info < (3, 0):
        out = ''.join([chr(b) for b in bytes])
    else:
        buf = bytearray(bytes)
        out = buf.decode('utf-8')
    return out

def getcodes(win):
    win.addstr('{}\n\n'.format(version_info))
    codes = []
    while True:
        try:
            ch = get_char(win)
            if ch == '[ESCAPE]':
                break
            else:
                win.addstr(ch)
        except KeyboardInterrupt:
            return codes
        codes.append(ch)

curses.wrapper(getcodes)
######################################################################
