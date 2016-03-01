"""
@author: francisparan
This script simulates the tree command in Linux,
but with an extra option for printing file contents
one by one.
"""

from __future__ import print_function
import os
import sys

# Python 3: raw_input => input
if sys.version_info.major == 3:
    raw_input = input


def __files(directory, show_hidden=False):

    if not os.path.isdir(directory):
        raise Exception('Directory not found: %s' % directory)

    files = os.listdir(directory)

    return filter(lambda f: not f.startswith('.'), files) if not show_hidden else files


def print_files(directory='.', show_hidden=False, recurse=False, padding=0):

    pad = ''.rjust(padding)

    for f in __files(directory, show_hidden):
        path = os.path.join(directory, f)
        file_output = "{} {}".format('-'.rjust(3), f)

        yield pad + file_output

        if recurse and (os.path.isdir(path) and os.access(path, os.R_OK)):
            for y in print_files(path, show_hidden, recurse, padding+5):
                yield y


def tree(directory, show_hidden=False, recurse=False, line_by_line=False):

    print(directory)

    for x in print_files(directory, show_hidden, recurse):

        if line_by_line:
            print(x, end=' ')

            if raw_input('').lower() == 'q':
                print('stopped...')
                break
        else:
            print(x)


if __name__ == '__main__':
    tree('..', recurse=True)
