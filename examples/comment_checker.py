"""
@author: francisparan
"""

import re
from sys import argv


def get_comment(lines, commentPattern ='^\#'):
    return [l for l in lines if re.match(commentPattern, l)]


def main():
    script, filename = argv

    with open(filename) as f:

        comment = False

        for line in f:
            if line.startswith('\"' * 3) or line.startswith("\'" * 3):
                comment = True

            if comment or re.match('^#', line):
                result = get_comment(f)

    print ''.join(result)

if __name__ == "__main__":
    print '''

    dfdfsdfdsff

    fdfsfdfsdf
    x =3
    """
    another comment
    """

    '''