
crf_learn -f 4 -p 4 -c 1 template_2gram ../data/7_10_train.tag ../result/model7_10_f4c1_2gram
crf_test -m ../result/model7_10_f4c1_2gram ../data/3_10_train.tag > ../result/3_10_f4c1_2gram.txt
