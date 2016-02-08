"""
@author: francisparan
This script is meant to demonstrate the use of rjust and center
for manipulating strings in stdout.
"""

width = 111

star_line = 6
for x in range(9):
    padding = 6
    star = '*'.rjust(padding) if star_line == 5 else '*'.center(padding)
    stars = ''.join([star for i in range(star_line)])

    if x % 2 > 0:
        stripes = '=' * 75

        if star_line == 5:
            stripes = ' ' * padding + stripes
        print stars + stripes
    else:
        print stars
    star_line = 5 if star_line == 6 else 6

for x in range(0, 7):
    print '=' * width
    print
