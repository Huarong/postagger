#!/usr/bin/env python
# -*- coding: utf-8 -*-


import util

def check_column_num(f):
    first_line = f.readline().strip()
    fix_size = len(first_line.split())
    for no, line in enumerate(f):
        line = line.strip()
        if line:
            size = len(line.split())
            if size != fix_size:
                print 'column number is not a fix number'
                print '%s: %s' % (no+2, line)
                return None
    print 'Column number is valid!'
    return None


def main():
    path = util.abs_path('data/crf_train.tag')
    with open(path) as f:
        check_column_num(f)
    return None


if __name__ == '__main__':
    main()