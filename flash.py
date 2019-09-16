import sys
import os
from typing import List

from serial.tools.list_ports import comports
from serial.tools.list_ports_common import ListPortInfo


def get_serial_port() -> ListPortInfo:
    while True:
        ports: List[ListPortInfo] = comports()
        for index, port in enumerate(ports):
            print('[%s]\t%s' % (index + 1, port))
        print('Enter a number between 1 and %s...' % len(ports))
        index = input('> ')
        try:
            index = int(index) - 1
        except ValueError:
            sys.stderr.write('Input must be a number!' + os.linesep + os.linesep)
            continue
        if index not in range(len(ports)):
            sys.stderr.write('Input must be between 1 and %s!' % len(ports)
                             + os.linesep + os.linesep)
            continue
        else:
            return ports[index]


def flash(port: ListPortInfo, file: str):
    cmd = 'avrdude'
    param = [
        '-v', '-p atmega328p', '-c arduino', '-P %s', '-b 115200', '-D',
        '-U', 'flash:w:%s:i'
    ]
    print(' '.join([cmd] + param) % (port.device, file))
    return os.system(' '.join([cmd] + param) % (port.device, file))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.stderr.write('Usage: python flash.py FILE' + os.linesep)
        sys.exit(2)

    file = sys.argv[1]
    port = get_serial_port()
    while True:
        ret = flash(port, file)
        if ret == 0:
            print('Success!')
        else:
            print('Failed! See output above...')
        print('Enter to continue, anything else to exit...')
        print('Notice: If you continue and the same port is still available, '
            'it will be used again without asking!')
        i = input('> ')
        if i == '':
            if port.device not in [p.device for p in comports()]:
                port = get_serial_port()
            else:
                print('Using same port again...')
            continue
        else:
            break