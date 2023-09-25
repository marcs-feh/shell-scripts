#!/usr/bin/env python
from subprocess import call
from sys import argv, exit
from math import floor

BACKLIGHT = '/sys/class/backlight/intel_backlight'
MAX_BRIGHTNESS = 21333 # Constant from /sys/class/backlight/...
MIN_BRIGHTNESS = floor(MAX_BRIGHTNESS * 0.05)

def get_brightness():
    br = 0.00
    with open(f'{BACKLIGHT}/brightness', 'r') as f:
        br = float(f.read())
    return float(br / MAX_BRIGHTNESS)

def set_brightness(lum : float):
    if lum > 1.0: lum = 1.0
    br = MAX_BRIGHTNESS * lum
    if br < MIN_BRIGHTNESS: br = MIN_BRIGHTNESS
    call(['sh','-c',f'echo {int(br)} > {BACKLIGHT}/brightness'])

def usage():
    print('brightness [inc|dec|set|get|reset|min|max] [0.00 ~ 1.00]')
    exit(1)

def main():
    if len(argv) < 2:
        usage()

    arg_opts = ['inc', 'dec', 'set']
    cur_br = get_brightness()
    cmd = str(argv[1])
    if cmd == 'reset':
        set_brightness(0.5)
    elif cmd == 'min':
        set_brightness(0.05)
    elif cmd == 'max':
        set_brightness(1.0)
    elif cmd == 'get':
        print(get_brightness())
    elif cmd in arg_opts:
        if len(argv) < 3:
            usage()
        try:
            cmd_val = float(argv[2])
        except ValueError:
            usage()
        if cmd == 'set':
            set_brightness(cmd_val)
        elif cmd == 'inc':
            set_brightness(get_brightness() + cmd_val)
        elif cmd == 'dec':
            set_brightness(get_brightness() - cmd_val)
    else:
        usage()

if __name__ == '__main__':
    main()
