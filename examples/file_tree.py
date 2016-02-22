"""
@author: francisparan
This script simulates the tree command in Linux,
but with an extra option for printing file contents
one by one.
"""

from __future__ import print_function
import os
import sys

if sys.version_info.major == 3:
    from builtins import input
    raw_input = input


def __files(directory, show_hidden=False):

    if not os.path.isdir(directory):
        print('Directory not found: %s' % directory)
        return ()

    files = [x for x in os.listdir(directory)]

    if not show_hidden:
        files = filter(lambda f: not f.startswith('.'), files)

    return (('-'.rjust(3) + ' ' + f, os.path.join(directory, f)) for f in files)


def print_files(directory='.', show_hidden=False, recurse=False, padding=0):

    pad = ''.rjust(padding)

    for f, p in __files(directory, show_hidden):
        
        yield pad + f

        if os.path.isdir(p) and recurse and os.access(p, os.R_OK):
            for y in print_files(p, show_hidden, recurse, padding+5):
                yield y


def tree(directory, show_hidden=False, recurse=False, one_by_one=False):

    print(directory)

    for x in print_files(directory, show_hidden, recurse):

        if one_by_one:
            print(x, end=' ')

            if raw_input('').lower() == 'q':
                print('stopped...')
                break
        else:
            print(x)


if __name__ == '__main__':
    tree('..', show_hidden=True)
