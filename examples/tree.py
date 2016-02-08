"""
@author: francisparan
This script simulates the tree command in Linux,
but with an extra option for printing file contents
one by one.
"""

import os


def __files(directory, show_hidden=False):

    files = [x for x in os.listdir(directory)]

    if not show_hidden:
        files = filter(lambda f: not f.startswith('.'), files)

    for f in files:
        yield '-'.rjust(3) + ' ' + f, os.path.join(directory, f)


def print_files(directory='.', show_hidden=False, recurse=False, padding=0):

    pad = ''.rjust(padding)

    for f, p in __files(directory, show_hidden):
        
        yield pad + f

        if os.path.isdir(p) and recurse and os.access(p, os.R_OK):
            for y in print_files(p, show_hidden, recurse, padding+5):
                yield y


def tree(directory, show_hidden=False, recurse=False, one_by_one=False):

    print directory

    for x in print_files(directory, show_hidden, recurse):

        if one_by_one:
            print x,

            if raw_input('').lower() == 'q':
                print 'stopped...'
                break

        else:
            print x


if __name__ == '__main__':
    tree('..', recurse=True)
