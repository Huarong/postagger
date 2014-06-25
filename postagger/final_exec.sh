
crf_learn -f 4 -p 4 -c 1.21 template_skip_2gram ../data/crf_train.tag ../result/model_train_f4c1.21_skip_2gram
crf_test -m ../result/model_train_f4c1.21_skip_2gram ../data/crf_test.tag > ../result/test_f4c1.21_skip_2gram.txt
