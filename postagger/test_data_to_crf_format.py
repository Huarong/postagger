#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import os

import util

def load_data(path):
    print 'Begin to load testing data ... ',
    lst = []
    with codecs.open(path, 'rb', encoding='utf-16') as f:
        for line in f:
            line = line.strip()
            if line:
                line_lst = line.split()
                lst.append(line_lst)
    print 'finish'
    return lst


def dump_as_crf_format(lst, path, placeholder='H'):
    print 'Begin to dump as crf data format ... ',
    with codecs.open(path, 'wb', encoding='utf-8') as f:
        for line_lst in lst:
            lines = ['%s %s%s' % (term, placeholder, os.linesep) for term in line_lst]
            lines.append(os.linesep)
            f.writelines(lines)
    print 'finish'
    return None


def main():
    in_path = util.abs_path('data/ckip_test_utf16.tag')
    out_path = util.abs_path('data/crf_test.tag')
    lst = load_data(in_path)
    dump_as_crf_format(lst, out_path)
    return None


if __name__ == '__main__':
    main()
