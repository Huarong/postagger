#!/usr/bin/env python
# -*- coding: utf-8 -*-


import util

def evaluate(path):
    total_num = 0
    correct = 0
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                total_num += 1
                term, answer, predict = line.split()
                if answer == predict:
                    correct += 1
    presion = float(correct) / total_num

    print 'Total line number: %d' % total_num
    print 'Correct line number: %d' % correct
    print 'Presion: %f' % presion
    return None


def main():
    path = util.abs_path('data/origin_train_test.txt')
    evaluate(path)
    return None


if __name__ == '__main__':
    main()