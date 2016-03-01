
from __future__ import print_function
import os
import sys

# Python 3: raw_input => input
if sys.version_info.major == 3:
    raw_input = input


class Tree:

    def __init__(self, depth=0, line_by_line=0):
        self.depth = depth
        self.line_by_line = line_by_line
        self.__end = '\n'
        self.level = 1
        self.files = 0
        self.directories = 0

    def get_files(self, directory, show_hidden=False):

        if not os.path.isdir(directory):
            raise Exception('Directory not found: %s' % directory)

        files = os.listdir(directory)

        return filter(lambda f: not f.startswith('.'), files) if not show_hidden else files

    def display_file(self, file_name, padding=0):
        pad = ''.rjust(padding)
        file_output = "{} {}".format('-'.rjust(3), file_name)
        print(pad + file_output, end = self.__end)

    def print_tree(self, directory='.', show_hidden=False, recurse=False, level=1):

        indent = 5 * (level-1)
        self.files += 1

        for f in self.get_files(directory, show_hidden):

            if self.line_by_line:
                self.__end = ' '
            
            self.display_file(f, padding=indent)

            if self.line_by_line and raw_input('').lower() == 'q':
                raise Exception

            path = os.path.join(directory, f)

            if recurse and (os.path.isdir(path) and os.access(path, os.R_OK)):
                if self.depth and level >= self.depth:
                    continue
                self.print_tree(path, show_hidden=show_hidden, recurse=recurse, level=level + 1)


def tree(directory='.', show_hidden=False, recurse=False, line_by_line=False, depth=0):
    if not os.path.isdir(directory):
        if os.path.isfile(directory):
            raise Exception('%s is a file' % directory)
        raise Exception('Directory not found: %s' % directory)

    print(directory)
    Tree(depth, line_by_line).print_tree(directory, show_hidden, recurse)


if __name__ == '__main__':
    tree()
