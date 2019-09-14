import sys
import os
from typing import List

from serial.tools.list_ports import comports
from serial.tools.list_ports_common import ListPortInfo


def get_serial_port() -> ListPortInfo:
    ports: List[ListPortInfo] = comports()
    while True:
        for index, port in enumerate(ports):
            print('[%s]\t%s' % (index + 1, port))
        print('Enter a number between 1 and %s' % len(ports))
        index = input('> ')
        try:
            index = int(index) - 1
        except ValueError:
            sys.stderr.write('Input must be a number' + os.linesep + os.linesep)
            continue
        if index not in range(len(ports)):
            sys.stderr.write('Input must be between 1 and %s' % len(ports)
                             + os.linesep + os.linesep)
            continue
        else:
            return ports[index]


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.stderr.write('Usage: python flash.py FILE' + os.linesep)
        sys.exit(2)

    port = get_serial_port()
    cmd = 'avrdude -v -p atmega328p -c arduino -P %s -b 115200 -D -U ' \
          'flash:w:%s:i'
    os.system(cmd % (port.device, sys.argv[1]))