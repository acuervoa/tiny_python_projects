#!/usr/bin/env python3
"""
Author : kuerbo <kuerbo@localhost>
Date   : 2022-06-19
Purpose: Howler (upper-cases input)
"""

import argparse
import os
import io
import sys


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler (upper-cases input)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input string or file')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text)
    else:
        args.text = io.StringIO(args.text + '\n')

    return args


def main():
    """Make a jazz noise here"""

    args = get_args()
    out_fh = open(args.outfile, 'w') if args.outfile else sys.stdout
    for line in args.text:
        out_fh.write(line.upper())
    out_fh.close()


if __name__ == '__main__':
    main()
