#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import os

import util

def load_data(path):
    print 'Begin to load training data ... ',
    lst = []
    with codecs.open(path, 'rb', encoding='utf-16') as f:
        for line in f:
            line_lst = []
            line = line.strip()
            if line:
                tokens = line.split()
                for token in tokens:
                    term, pos = token.split('/')
                    # term may be blank
                    if not term.strip():
                        continue
                    # pos may be blank
                    if not pos.strip():
                        pos = 'NULL'
                    line_lst.append((term, pos))
                lst.append(line_lst)
    print 'finish'
    return lst


def dump_as_crf_format(lst, path):
    print 'Begin to dump as crf data format ... ',
    with codecs.open(path, 'wb', encoding='utf-8') as f:
        for line_lst in lst:
            lines = ['%s %s%s' % (term, pos, os.linesep) for term, pos in line_lst]
            lines.append(os.linesep)
            f.writelines(lines)
    print 'finish'
    return None


def main():
    in_path = util.abs_path('data/ckip_train_utf16.tag')
    out_path = util.abs_path('data/crf_train.tag')
    lst = load_data(in_path)
    dump_as_crf_format(lst, out_path)
    return None


if __name__ == '__main__':
    main()
