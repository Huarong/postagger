#!/usr/bin/env python
# -*- coding: utf-8 -*-


import util


def split(path, small_path, large_path, parts=10):
    with open(path) as f:
        for index, line in enumerate(f):
            pass
        total_line_num = index
        print 'Total line number is: %d' % total_line_num
        a_part_num = total_line_num / parts
        f.seek(0)
        for i in range(a_part_num - 1):
            line = f.readline()
        # find a blank line
        line_offset = a_part_num - 1
        offset = f.tell()
        print 'Suppose spliting line number: %d' % line_offset
        while line.strip():
            line = f.readline()
            line_offset += 1
            offset = f.tell()
        print 'Actual spliting line number: %d' % line_offset
        f.seek(0)
        with open(small_path, 'wb') as fs:
            fs.write(f.read(offset))
        with open(large_path, 'wb') as fl:
            fl.write(f.read())
    return None


def main():
    parts = 10
    train_path = util.abs_path('data/crf_train.tag')
    out_path_train = util.abs_path('data/%d_%d_train.tag' % (parts - 1, parts))
    out_path_validation = util.abs_path('data/1_%d_train.tag' % parts)
    split(train_path, out_path_validation, out_path_train, parts=parts)


if __name__ == '__main__':
    main()