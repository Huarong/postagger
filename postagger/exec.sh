
crf_learn -f 4 -p 2 template_skip_2gram ../data/9_10_train.tag ../result/model9_10_f4c1_skip_2gram
crf_test -m ../result/model9_10_f4c1_skip_2gram ../data/1_10_train.tag > ../result/1_10_f4c1_skip_2gram.txt
