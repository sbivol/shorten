#!/usr/bin/python3

"""
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program. If not, see <https://www.gnu.org/licenses/>.
"""

import sys

def shorten(string, dir_len="80"):
    string = string.strip()
    length = abs(int(dir_len)) - 1
    if len(string) <= length:
        return string

    direction = dir_len[0]
    if direction.isdigit():
        direction = ""

    if direction == "":
        first_slice_len = int(length / 2)
        second_slice_len = length - first_slice_len
        return '{0}…{1}'.format(string[:first_slice_len], string[-second_slice_len:])

    if direction == "-":
        return '{0}…'.format(string[:length])

    if direction == "+":
        return '…{0}'.format(string[-length:])


def get_terminal_width():
    import shutil
    return shutil.get_terminal_size()[0]


if __name__ == "__main__":
    # We are not reading from STDIN
    if sys.stdin.isatty():
        # If more than one parameter were supplied,
        # the first parameter is {[direction][length]}
        if len(sys.argv) > 2:
            if sys.argv[1] in ("-", "+"):
                length = sys.argv[1] + str(get_terminal_width())
            else:
                length = sys.argv[1]
        else:
            length = str(get_terminal_width())

        # The last parameter is the string to shorten
        if len(sys.argv) > 1:
            string = sys.argv[-1]

        print(shorten(string, length))
    else:
        if len(sys.argv) == 2:
            if sys.argv[1] in ("-", "+"):
                length = sys.argv[1] + str(get_terminal_width())
            else:
                length = sys.argv[1]
        else:
            length = str(get_terminal_width())

        for string in sys.stdin:
            print(shorten(string, length))
