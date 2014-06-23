第一次运行
使用所有的训练数据进行训练，使用得到的模型预测训练数据正确率

结果：
hhr@jyy-master:~/myapps/postagger/postagger$ ./eval.py ../result/origin_train_test.txt 
Total line number: 721549
Correct line number: 694124
Presion: 0.961991


第二次运行
Number of sentences: 84982
Number of features:  3601380
Number of thread(s): 2
Freq:                4
eta:                 0.00010
C:                   1.00000
shrinking size:      20
训练数据的1/10份
f: 4
p: 2
共迭代211次
运行时间： 36248 s

结果：
hhr@jyy-master:~/myapps/postagger/postagger$ ./eval.py ../result/1_10.txt 
Total line number: 72385
Correct line number: 65291
Presion: 0.901996


第三次以运行
Number of sentences: 84982
Number of features:  3601380
Number of thread(s): 4
Freq:                4
eta:                 0.00010
C:                   1.50000
shrinking size:      20

迭代 276次
运行时间： 24965 s

结果：
hhr@jyy-master:~/myapps/postagger/postagger$ ./eval.py ../result/1_10_f4c1.5.txt 
Total line number: 72385
Correct line number: 65440
Presion: 0.904055


第四次运行
Number of sentences: 84982
Number of features:  3601380
Number of thread(s): 2
Freq:                4
eta:                 0.00010
C:                   2.00000
shrinking size:      20

迭代： 273次
运行时间： 47043 s

结果：
Total line number: 72385
Correct line number: 65473
Presion: 0.904511

第五次运行

特征:
# Unigram
U00:%x[-2,0]
U01:%x[-1,0]
U02:%x[0,0]
U03:%x[1,0]
U04:%x[2,0]
U08:%x[-1,0]/%x[0,0]
U09:%x[0,0]/%x[1,0]


Number of sentences: 84982
Number of features:  6063420
Number of thread(s): 2
Freq:                4
eta:                 0.00010
C:                   1.00000
shrinking size:      20

迭代：226次
运行时间：38869 s

结果：
Total line number: 72385
Correct line number: 65410
Presion: 0.903640

第六次运行

# Unigram
U00:%x[-2,0]
U01:%x[-1,0]
U02:%x[0,0]
U03:%x[1,0]
U04:%x[2,0]
U08:%x[-1,0]/%x[0,0]
U09:%x[0,0]/%x[1,0]
U10:%x[-2,0]/%x[0,0]
U11:%x[0,0]/%x[2,0]

Number of sentences: 84982
Number of features:  8081100
Number of thread(s): 2
Freq:                4
eta:                 0.00010
C:                   1.00000
shrinking size:      20

迭代： 207次
运行时间：35468 s

结果：
Total line number: 72385
Correct line number: 65383
Presion: 0.903267

