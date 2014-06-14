
crf_learn -f 4 -p 2 -c 2 template ../data/9_10_train.tag ../result/model9_10_f4c2
crf_test -m ../result/model9_10_f4c2 ../data/1_10_train.tag > ../result/1_10_f4c2.txt
