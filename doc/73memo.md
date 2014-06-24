第一次运行：

特征：

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

crf_learn -f 4 -p 2 -c 1.0 template_skip_2gram ../data/7_10_train.tag ../result/model7_10_f4c1_skip_2gram
crf_test -m ../result/model7_10_f4c1_skip_2gram ../data/3_10_train.tag > ../result/3_10_f4c1_skip_2gram.txt

Number of sentences: 65466
Number of features:  6444780
Number of thread(s): 2
Freq:                4
eta:                 0.00010
C:                   1.00000
shrinking size:      20

迭代次数:195
运行时间：25743 s

结果：

hhr@jyy-master:~/myapps/postagger/postagger$ perl conlleval.pl -r -d '\t' < ../result/3_10_f4c1_skip_2gram.txt 
processed 216014 tokens with 216014 phrases; found: 216014 phrases; correct: 190205.
accuracy:  88.05%; precision:  88.05%; recall:  88.05%; FB1:  88.05
                A: precision:  88.87%; recall:  57.57%; FB1:  69.87  548
    COLONCATEGORY: precision: 100.00%; recall: 100.00%; FB1: 100.00  1337
    COMMACATEGORY: precision: 100.00%; recall:  99.98%; FB1:  99.99  18091
              Caa: precision:  94.22%; recall:  91.00%; FB1:  92.58  1974
              Cab: precision:  94.38%; recall:  98.33%; FB1:  96.31  249
              Cba: precision: 100.00%; recall: 100.00%; FB1: 100.00  32
              Cbb: precision:  97.68%; recall:  94.72%; FB1:  96.18  4484
                D: precision:  93.48%; recall:  94.86%; FB1:  94.17  18831
     DASHCATEGORY: precision: 100.00%; recall: 100.00%; FB1: 100.00  43
               DE: precision:  98.76%; recall:  98.91%; FB1:  98.83  11898
               Da: precision:  96.21%; recall:  93.10%; FB1:  94.63  897
              Dfa: precision:  97.41%; recall:  93.96%; FB1:  95.65  1582
              Dfb: precision: 100.00%; recall:  51.85%; FB1:  68.29  28
               Di: precision:  96.64%; recall:  95.13%; FB1:  95.88  2444
               Dk: precision:  88.37%; recall:  68.16%; FB1:  76.96  172
      ETCCATEGORY: precision: 100.00%; recall: 100.00%; FB1: 100.00  126
EXCLAMATIONCATEGORY: precision:   0.00%; recall:   0.00%; FB1:   0.00  0
EXCLANATIONCATEGORY: precision: 100.00%; recall:  99.84%; FB1:  99.92  608
               FW: precision:  21.18%; recall:  32.53%; FB1:  25.65  510
                I: precision:  97.67%; recall:  76.83%; FB1:  86.01  129
             NULL: precision:  97.74%; recall:  96.74%; FB1:  97.24  486
               Na: precision:  72.33%; recall:  95.06%; FB1:  82.15  47386
               Nb: precision:  78.11%; recall:  29.81%; FB1:  43.15  1649
               Nc: precision:  89.72%; recall:  67.23%; FB1:  76.87  5281
              Ncd: precision:  81.76%; recall:  79.98%; FB1:  80.86  1612
               Nd: precision:  92.98%; recall:  74.93%; FB1:  82.99  2736
              Nep: precision:  99.59%; recall:  99.19%; FB1:  99.39  2458
             Neqa: precision:  98.54%; recall:  90.00%; FB1:  94.08  1855
             Neqb: precision:  85.19%; recall:  67.65%; FB1:  75.41  27
              Nes: precision:  93.77%; recall:  94.70%; FB1:  94.23  1124
              Neu: precision:  95.87%; recall:  93.44%; FB1:  94.64  5040
               Nf: precision:  94.21%; recall:  96.55%; FB1:  95.37  5592
               Ng: precision:  90.80%; recall:  88.17%; FB1:  89.47  2619
               Nh: precision:  99.89%; recall:  97.67%; FB1:  98.76  6161
               Nv: precision:  65.94%; recall:  40.40%; FB1:  50.10  1876
                P: precision:  92.09%; recall:  92.65%; FB1:  92.37  7766
PARENTHESISCATEGORY: precision: 100.00%; recall:  99.98%; FB1:  99.99  4026
    PAUSECATEGORY: precision: 100.00%; recall:  99.94%; FB1:  99.97  1652
   PERIODCATEGORY: precision: 100.00%; recall: 100.00%; FB1: 100.00  8094
 QUESTIONCATEGORY: precision:  99.04%; recall:  99.86%; FB1:  99.45  726
SEMICOLONCATEGORY: precision: 100.00%; recall:  94.04%; FB1:  96.93  268
              SHI: precision: 100.00%; recall:  99.88%; FB1:  99.94  3210
 SPCHANGECATEGORY: precision: 100.00%; recall:  98.28%; FB1:  99.13  228
                T: precision:  87.53%; recall:  88.46%; FB1:  87.99  2005
               VA: precision:  74.61%; recall:  48.09%; FB1:  58.49  2182
              VAC: precision:  89.29%; recall:  39.06%; FB1:  54.35  28
               VB: precision:  87.80%; recall:  18.95%; FB1:  31.17  82
               VC: precision:  73.65%; recall:  78.62%; FB1:  76.05  11323
              VCL: precision:  81.82%; recall:  61.15%; FB1:  69.99  858
               VD: precision:  86.35%; recall:  63.15%; FB1:  72.95  381
               VE: precision:  94.29%; recall:  81.75%; FB1:  87.57  3711
               VF: precision:  96.54%; recall:  67.86%; FB1:  79.69  433
               VG: precision:  87.07%; recall:  71.21%; FB1:  78.35  1361
               VH: precision:  79.08%; recall:  74.98%; FB1:  76.98  10325
              VHC: precision:  95.22%; recall:  59.25%; FB1:  73.05  481
               VI: precision:  97.50%; recall:  25.49%; FB1:  40.41  40
               VJ: precision:  91.60%; recall:  70.23%; FB1:  79.50  2238
               VK: precision:  97.69%; recall:  85.56%; FB1:  91.22  2075
               VL: precision:  97.36%; recall:  82.76%; FB1:  89.47  947
              V_2: precision:  97.75%; recall:  99.88%; FB1:  98.80  1689
hhr@jyy-master:~/myapps/postagger/postagger$ 
               Nf: precision:  94.21%; recall:  96.55%; FB1:  95.37  5592
               Ng: precision:  90.80%; recall:  88.17%; FB1:  89.47  2619
               Nh: precision:  99.89%; recall:  97.67%; FB1:  98.76  6161
               Nv: precision:  65.94%; recall:  40.40%; FB1:  50.10  1876
                P: precision:  92.09%; recall:  92.65%; FB1:  92.37  7766
PARENTHESISCATEGORY: precision: 100.00%; recall:  99.98%; FB1:  99.99  4026
    PAUSECATEGORY: precision: 100.00%; recall:  99.94%; FB1:  99.97  1652
   PERIODCATEGORY: precision: 100.00%; recall: 100.00%; FB1: 100.00  8094
 QUESTIONCATEGORY: precision:  99.04%; recall:  99.86%; FB1:  99.45  726
SEMICOLONCATEGORY: precision: 100.00%; recall:  94.04%; FB1:  96.93  268
              SHI: precision: 100.00%; recall:  99.88%; FB1:  99.94  3210
 SPCHANGECATEGORY: precision: 100.00%; recall:  98.28%; FB1:  99.13  228
                T: precision:  87.53%; recall:  88.46%; FB1:  87.99  2005
               VA: precision:  74.61%; recall:  48.09%; FB1:  58.49  2182
              VAC: precision:  89.29%; recall:  39.06%; FB1:  54.35  28
               VB: precision:  87.80%; recall:  18.95%; FB1:  31.17  82
               VC: precision:  73.65%; recall:  78.62%; FB1:  76.05  11323
              VCL: precision:  81.82%; recall:  61.15%; FB1:  69.99  858
               VD: precision:  86.35%; recall:  63.15%; FB1:  72.95  381
               VE: precision:  94.29%; recall:  81.75%; FB1:  87.57  3711
               VF: precision:  96.54%; recall:  67.86%; FB1:  79.69  433
               VG: precision:  87.07%; recall:  71.21%; FB1:  78.35  1361
               VH: precision:  79.08%; recall:  74.98%; FB1:  76.98  10325
              VHC: precision:  95.22%; recall:  59.25%; FB1:  73.05  481
               VI: precision:  97.50%; recall:  25.49%; FB1:  40.41  40
               VJ: precision:  91.60%; recall:  70.23%; FB1:  79.50  2238
               VK: precision:  97.69%; recall:  85.56%; FB1:  91.22  2075
               VL: precision:  97.36%; recall:  82.76%; FB1:  89.47  947
              V_2: precision:  97.75%; recall:  99.88%; FB1:  98.80  1689

第二次运行：

特征：

# Unigram
U00:%x[-2,0]
U01:%x[-1,0]
U02:%x[0,0]
U03:%x[1,0]
U04:%x[2,0]
U05:%x[-2,0]/%x[-1,0]/%x[0,0]
U06:%x[-1,0]/%x[0,0]/%x[1,0]
U07:%x[0,0]/%x[1,0]/%x[2,0]
U08:%x[-1,0]/%x[0,0]
U09:%x[0,0]/%x[1,0]
U10:%x[-2,0]/%x[0,0]
U11:%x[0,0]/%x[2,0]

crf_learn -f 4 -p 4 -c 1 template_3gram ../data/7_10_train.tag ../result/model7_10_f4c1_3gram
crf_test -m ../result/model7_10_f4c1_3gram ../data/3_10_train.tag > ../result/3_10_f4c1_3gram.txt

迭代次数: 199
运行时间：14669 s

结果：

hhr@jyy-master:~/myapps/postagger/postagger$ perl conlleval.pl -r -d '\t' < ../result/3_10_f4c1_3gram.txt
processed 216014 tokens with 216014 phrases; found: 216014 phrases; correct: 190098.
accuracy:  88.00%; precision:  88.00%; recall:  88.00%; FB1:  88.00
                A: precision:  89.21%; recall:  57.68%; FB1:  70.06  547
    COLONCATEGORY: precision: 100.00%; recall: 100.00%; FB1: 100.00  1337
    COMMACATEGORY: precision: 100.00%; recall:  99.98%; FB1:  99.99  18091
              Caa: precision:  93.95%; recall:  91.10%; FB1:  92.50  1982
              Cab: precision:  94.38%; recall:  98.33%; FB1:  96.31  249
              Cba: precision: 100.00%; recall: 100.00%; FB1: 100.00  32
              Cbb: precision:  97.74%; recall:  94.42%; FB1:  96.05  4467
                D: precision:  93.36%; recall:  94.87%; FB1:  94.11  18856
     DASHCATEGORY: precision: 100.00%; recall: 100.00%; FB1: 100.00  43
               DE: precision:  98.76%; recall:  98.91%; FB1:  98.84  11897
               Da: precision:  96.21%; recall:  93.10%; FB1:  94.63  897
              Dfa: precision:  97.23%; recall:  94.09%; FB1:  95.63  1587
              Dfb: precision:  96.43%; recall:  50.00%; FB1:  65.85  28
               Di: precision:  96.73%; recall:  95.21%; FB1:  95.96  2444
               Dk: precision:  87.36%; recall:  68.16%; FB1:  76.57  174
      ETCCATEGORY: precision: 100.00%; recall: 100.00%; FB1: 100.00  126
EXCLAMATIONCATEGORY: precision:   0.00%; recall:   0.00%; FB1:   0.00  0
EXCLANATIONCATEGORY: precision: 100.00%; recall:  99.84%; FB1:  99.92  608
               FW: precision:  20.08%; recall:  32.23%; FB1:  24.74  533
                I: precision:  97.00%; recall:  59.15%; FB1:  73.48  100
             NULL: precision:  97.74%; recall:  96.74%; FB1:  97.24  486
               Na: precision:  72.44%; recall:  94.94%; FB1:  82.18  47255
               Nb: precision:  77.62%; recall:  29.95%; FB1:  43.22  1667
               Nc: precision:  89.55%; recall:  67.22%; FB1:  76.79  5290
              Ncd: precision:  82.36%; recall:  79.61%; FB1:  80.96  1593
               Nd: precision:  93.20%; recall:  74.73%; FB1:  82.95  2722
              Nep: precision:  99.59%; recall:  99.15%; FB1:  99.37  2457
             Neqa: precision:  98.55%; recall:  90.15%; FB1:  94.16  1858
             Neqb: precision:  84.62%; recall:  64.71%; FB1:  73.33  26
              Nes: precision:  94.08%; recall:  94.16%; FB1:  94.12  1114
              Neu: precision:  95.89%; recall:  93.46%; FB1:  94.66  5040
               Nf: precision:  94.19%; recall:  96.55%; FB1:  95.36  5593
               Ng: precision:  90.64%; recall:  88.69%; FB1:  89.66  2639
               Nh: precision:  99.90%; recall:  97.64%; FB1:  98.76  6158
               Nv: precision:  65.57%; recall:  40.30%; FB1:  49.92  1882
                P: precision:  92.25%; recall:  92.42%; FB1:  92.34  7733
PARENTHESISCATEGORY: precision: 100.00%; recall:  99.98%; FB1:  99.99  4026
    PAUSECATEGORY: precision: 100.00%; recall:  99.94%; FB1:  99.97  1652
   PERIODCATEGORY: precision: 100.00%; recall: 100.00%; FB1: 100.00  8094
 QUESTIONCATEGORY: precision:  99.31%; recall:  99.86%; FB1:  99.58  724
SEMICOLONCATEGORY: precision: 100.00%; recall:  94.04%; FB1:  96.93  268
              SHI: precision: 100.00%; recall:  99.84%; FB1:  99.92  3209
 SPCHANGECATEGORY: precision: 100.00%; recall:  97.41%; FB1:  98.69  226
                T: precision:  87.37%; recall:  88.91%; FB1:  88.13  2019
               VA: precision:  74.88%; recall:  47.83%; FB1:  58.37  2162
              VAC: precision:  88.89%; recall:  37.50%; FB1:  52.75  27
               VB: precision:  87.34%; recall:  18.16%; FB1:  30.07  79
               VC: precision:  72.96%; recall:  78.82%; FB1:  75.78  11458
              VCL: precision:  81.65%; recall:  61.24%; FB1:  69.99  861
               VD: precision:  86.16%; recall:  63.34%; FB1:  73.01  383
               VE: precision:  94.26%; recall:  81.78%; FB1:  87.58  3713
               VF: precision:  96.98%; recall:  67.69%; FB1:  79.73  430
               VG: precision:  86.73%; recall:  71.45%; FB1:  78.35  1371
               VH: precision:  78.84%; recall:  74.88%; FB1:  76.81  10342
              VHC: precision:  95.17%; recall:  58.60%; FB1:  72.54  476
               VI: precision:  95.12%; recall:  25.49%; FB1:  40.21  41
               VJ: precision:  91.54%; recall:  70.09%; FB1:  79.39  2235
               VK: precision:  97.68%; recall:  85.48%; FB1:  91.18  2073
               VL: precision:  97.35%; recall:  82.59%; FB1:  89.36  945
              V_2: precision:  97.75%; recall:  99.88%; FB1:  98.80  1689


第三次运行：

特征：

# Unigram
U21:%x[-3,0]
U00:%x[-2,0]
U01:%x[-1,0]
U02:%x[0,0]
U03:%x[1,0]
U04:%x[2,0]
U22:%x[3,0]
U05:%x[-2,0]/%x[-1,0]/%x[0,0]
U06:%x[-1,0]/%x[0,0]/%x[1,0]
U07:%x[0,0]/%x[1,0]/%x[2,0]
U08:%x[-1,0]/%x[0,0]
U09:%x[0,0]/%x[1,0]
U10:%x[-2,0]/%x[0,0]
U11:%x[0,0]/%x[2,0]

crf_learn -f 4 -p 4 -c 1 template_4gram ../data/7_10_train.tag ../result/model7_10_f4c1_4gram
crf_test -m ../result/model7_10_f4c1_4gram ../data/3_10_train.tag > ../result/3_10_f4c1_4gram.txt

Number of sentences: 65466
Number of features:  8671200
Number of thread(s): 4
Freq:                4
eta:                 0.00010
C:                   1.00000
shrinking size:      20

迭代次数:219
运行时间：16923 s

结果：

hhr@jyy-master:~/myapps/postagger/postagger$ perl conlleval.pl -r -d '\t' < ../result/3_10_f4c1_4gram.txt
processed 216014 tokens with 216014 phrases; found: 216014 phrases; correct: 189678.
accuracy:  87.81%; precision:  87.81%; recall:  87.81%; FB1:  87.81
                A: precision:  88.89%; recall:  55.79%; FB1:  68.55  531
    COLONCATEGORY: precision: 100.00%; recall:  99.93%; FB1:  99.96  1336
    COMMACATEGORY: precision: 100.00%; recall:  99.97%; FB1:  99.99  18090
              Caa: precision:  94.15%; recall:  90.56%; FB1:  92.32  1966
              Cab: precision:  94.69%; recall:  97.07%; FB1:  95.87  245
              Cba: precision: 100.00%; recall: 100.00%; FB1: 100.00  32
              Cbb: precision:  97.72%; recall:  94.55%; FB1:  96.11  4474
                D: precision:  93.02%; recall:  94.76%; FB1:  93.88  18903
     DASHCATEGORY: precision: 100.00%; recall: 100.00%; FB1: 100.00  43
               DE: precision:  98.71%; recall:  98.91%; FB1:  98.81  11905
               Da: precision:  96.52%; recall:  92.88%; FB1:  94.67  892
              Dfa: precision:  97.39%; recall:  93.23%; FB1:  95.26  1570
              Dfb: precision:  96.55%; recall:  51.85%; FB1:  67.47  29
               Di: precision:  96.48%; recall:  95.01%; FB1:  95.74  2445
               Dk: precision:  88.00%; recall:  69.06%; FB1:  77.39  175
      ETCCATEGORY: precision: 100.00%; recall: 100.00%; FB1: 100.00  126
EXCLAMATIONCATEGORY: precision:   0.00%; recall:   0.00%; FB1:   0.00  0
EXCLANATIONCATEGORY: precision: 100.00%; recall:  99.84%; FB1:  99.92  608
               FW: precision:  21.51%; recall:  28.31%; FB1:  24.45  437
                I: precision:  96.12%; recall:  60.37%; FB1:  74.16  103
             NULL: precision:  98.14%; recall:  96.74%; FB1:  97.44  484
               Na: precision:  72.53%; recall:  94.60%; FB1:  82.11  47026
               Nb: precision:  75.95%; recall:  30.85%; FB1:  43.88  1755
               Nc: precision:  87.34%; recall:  67.43%; FB1:  76.11  5441
              Ncd: precision:  81.93%; recall:  79.25%; FB1:  80.57  1594
               Nd: precision:  92.94%; recall:  74.08%; FB1:  82.45  2706
              Nep: precision:  99.59%; recall:  99.15%; FB1:  99.37  2457
             Neqa: precision:  98.60%; recall:  89.86%; FB1:  94.02  1851
             Neqb: precision:  83.33%; recall:  58.82%; FB1:  68.97  24
              Nes: precision:  94.22%; recall:  93.80%; FB1:  94.01  1108
              Neu: precision:  95.88%; recall:  93.08%; FB1:  94.46  5020
               Nf: precision:  93.95%; recall:  96.15%; FB1:  95.04  5584
               Ng: precision:  90.86%; recall:  88.10%; FB1:  89.46  2615
               Nh: precision:  99.89%; recall:  97.57%; FB1:  98.72  6155
               Nv: precision:  63.05%; recall:  40.79%; FB1:  49.53  1981
                P: precision:  92.07%; recall:  92.25%; FB1:  92.16  7734
PARENTHESISCATEGORY: precision: 100.00%; recall:  99.98%; FB1:  99.99  4026
    PAUSECATEGORY: precision: 100.00%; recall:  99.94%; FB1:  99.97  1652
   PERIODCATEGORY: precision: 100.00%; recall: 100.00%; FB1: 100.00  8094
 QUESTIONCATEGORY: precision:  99.31%; recall:  99.86%; FB1:  99.58  724
SEMICOLONCATEGORY: precision: 100.00%; recall:  94.04%; FB1:  96.93  268
              SHI: precision: 100.00%; recall:  99.78%; FB1:  99.89  3207
 SPCHANGECATEGORY: precision: 100.00%; recall:  97.84%; FB1:  98.91  227
                T: precision:  87.33%; recall:  87.90%; FB1:  87.62  1997
               VA: precision:  72.77%; recall:  48.01%; FB1:  57.85  2233
              VAC: precision:  90.48%; recall:  29.69%; FB1:  44.71  21
               VB: precision:  85.37%; recall:  18.42%; FB1:  30.30  82
               VC: precision:  72.70%; recall:  78.53%; FB1:  75.50  11458
              VCL: precision:  79.79%; recall:  59.84%; FB1:  68.39  861
               VD: precision:  84.88%; recall:  61.42%; FB1:  71.27  377
               VE: precision:  94.09%; recall:  81.07%; FB1:  87.10  3688
               VF: precision:  97.67%; recall:  68.02%; FB1:  80.19  429
               VG: precision:  85.71%; recall:  71.03%; FB1:  77.69  1379
               VH: precision:  78.13%; recall:  74.78%; FB1:  76.42  10422
              VHC: precision:  95.95%; recall:  58.21%; FB1:  72.46  469
               VI: precision:  94.44%; recall:  22.22%; FB1:  35.98  36
               VJ: precision:  90.73%; recall:  69.37%; FB1:  78.63  2232
               VK: precision:  97.47%; recall:  84.59%; FB1:  90.58  2056
               VL: precision:  96.92%; recall:  81.96%; FB1:  88.81  942
              V_2: precision:  97.75%; recall:  99.88%; FB1:  98.80  1689

第四次运行：

特征：

# Unigram
U00:%x[-2,0]
U01:%x[-1,0]
U02:%x[0,0]
U03:%x[1,0]
U04:%x[2,0]

crf_learn -f 4 -p 4 -c 1 template_2gram ../data/7_10_train.tag ../result/model7_10_f4c1_2gram
crf_test -m ../result/model7_10_f4c1_2gram ../data/3_10_train.tag > ../result/3_10_f4c1_2gram.txt

Number of sentences: 65466
Number of features:  2958240
Number of thread(s): 4
Freq:                4
eta:                 0.00010
C:                   1.00000
shrinking size:      20